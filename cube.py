# glass_cube.py
# 실행: python glass_cube.py
# 터미널에서 유리 느낌의 회전 큐브 (ASCII)
import math, os, sys, time, shutil

# ------------------ 설정 (원하면 여기만 조정) ------------------
SIZE = 3.2            # 큐브 반쪽 길이
SUBDIV = 20           # 면 샘플 해상도 (값 증가 -> 더 촘촘, 느려짐)
EDGE_THICKNESS = 2    # 엣지 굵기 (정수 권장)
FPS = 22
DISTANCE = 16.0
SCALE = 36.0
EDGE_CHAR = "@"       # 테두리 문자
VERTEX_CHAR = "*"     # 꼭짓점 반짝임 문자
# ASCII 그라데이션: 어두움 -> 밝음 (길이가 길수록 세밀)
GRADIENT = list(" .,:;i1tfLCG08@")
# 빛(태양) 방향 (세계 좌표)
LIGHT_DIR = (0.5, 0.7, -0.4)
# 스페큘러 세기 / 샤이니니스 (클수록 작고 날카로운 하이라이트)
SPEC_POWER = 50.0
SPEC_STRENGTH = 1.0
# 배경 반사 패턴 파라미터
ENV_WAVE = 8.0
ENV_STREAK = 20.0
# ---------------------------------------------------------------

def term_size(default_w=120, default_h=50):
    try:
        w, h = shutil.get_terminal_size()
        # 높이는 문자 종횡비 고려하여 약간 줄임
        return max(40, w), max(20, int(h * 0.65))
    except:
        return default_w, default_h

def norm(v):
    x,y,z = v
    m = math.sqrt(x*x + y*y + z*z) or 1.0
    return (x/m, y/m, z/m)
def dot(a,b): return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
def reflect(I, N):
    # 반사 벡터 R = I - 2*(I·N)*N
    d = 2 * dot(I, N)
    return (I[0] - d*N[0], I[1] - d*N[1], I[2] - d*N[2])

LIGHT_DIR = norm(LIGHT_DIR)

def make_vertices(s):
    return [
        [-s, -s, -s],
        [-s, -s,  s],
        [-s,  s, -s],
        [-s,  s,  s],
        [ s, -s, -s],
        [ s, -s,  s],
        [ s,  s, -s],
        [ s,  s,  s],
    ]

EDGES = [
    (0,1),(0,2),(0,4),
    (1,3),(1,5),
    (2,3),(2,6),
    (3,7),
    (4,5),(4,6),
    (5,7),
    (6,7)
]

def rotate(x,y,z, rx, ry, rz):
    cosx, sinx = math.cos(rx), math.sin(rx)
    y, z = y*cosx - z*sinx, y*sinx + z*cosx
    cosy, siny = math.cos(ry), math.sin(ry)
    x, z = x*cosy + z*siny, -x*siny + z*cosy
    cosz, sinz = math.cos(rz), math.sin(rz)
    x, y = x*cosz - y*sinz, x*sinz + y*cosz
    return x, y, z

def project(x,y,z, width, height, scale=SCALE, distance=DISTANCE):
    factor = scale / (z + distance)
    px = int(width/2 + x*factor)
    py = int(height/2 - y*factor)
    return px, py, z

def sample_cube_surfaces(size, subdiv):
    s = size
    n = subdiv
    pts = []
    rng = [i/(n-1) for i in range(n)]
    for t in rng:
        for u in rng:
            pts.append(( s, (t*2-1)*s, (u*2-1)*s))
            pts.append((-s, (t*2-1)*s, (u*2-1)*s))
            pts.append(((t*2-1)*s,  s, (u*2-1)*s))
            pts.append(((t*2-1)*s, -s, (u*2-1)*s))
            pts.append(((t*2-1)*s, (u*2-1)*s,  s))
            pts.append(((t*2-1)*s, (u*2-1)*s, -s))
    return pts

def interpolate(a,b,steps):
    ax,ay,az = a; bx,by,bz = b
    for i in range(steps+1):
        t = i/steps
        yield (ax + (bx-ax)*t, ay + (by-ay)*t, az + (bz-az)*t)

# 가짜 환경 맵: 반사 방향으로부터 밝기(0..1)를 계산
def env_sample(ref):
    # ref: normalized reflection vector (rx, ry, rz)
    rx, ry, rz = ref
    # 수평으로는 파동성(구름/하늘), 수직으로는 그라데이션(밝은 상공/어두운 지면)
    u = 0.5 + 0.5 * rx
    v = 0.5 + 0.5 * ry
    # 파동 무늬 + 스트릭(빛줄기)
    wave = 0.5 + 0.5 * math.sin((u * ENV_WAVE + v * 2.3) * math.pi * 2.0)
    streak = 0.5 + 0.5 * math.sin((u*ENV_STREAK) * 2.0 * math.pi)
    base = 0.35 + 0.65 * v  # 위쪽이 더 밝음
    brightness = base * (0.6 + 0.4 * wave) * (0.8 + 0.2 * streak)
    # 소소한 노이즈 느낌 추가
    brightness += 0.03 * math.sin(17.0*rx + 13.0*ry + 7.0*rz)
    return max(0.0, min(1.0, brightness))

def draw_frame(vertices, edges, fill_points, rx, ry, rz, width, height):
    screen = [[" " for _ in range(width)] for _ in range(height)]
    depth = [[-1e9 for _ in range(width)] for _ in range(height)]

    # 1) 면 채우기: env 반사 + Lambert diffuse + Fresnel
    for (x,y,z) in fill_points:
        xr, yr, zr = rotate(x,y,z, rx, ry, rz)
        px, py, zcam = project(xr, yr, zr, width, height)
        if not (0 <= px < width and 0 <= py < height): continue

        # face normal (근사: 절대값이 큰 축이 face를 결정)
        absx, absy, absz = abs(x), abs(y), abs(z)
        if absx >= absy and absx >= absz:
            N = (math.copysign(1, x), 0.0, 0.0)
        elif absy >= absx and absy >= absz:
            N = (0.0, math.copysign(1, y), 0.0)
        else:
            N = (0.0, 0.0, math.copysign(1, z))

        # 카메라(시선) 벡터: camera at (0,0,-DISTANCE), point in camera space is (xr,yr,zr)
        V = norm((-xr, -yr, -zr))
        # 반사 벡터
        R = reflect(V, N)
        Rn = norm(R)

        # Lambert diffuse
        diffuse = max(0.0, dot(N, LIGHT_DIR))
        # Fresnel(간단): 시선과 법선 각도에 따라 반사 증가
        fresnel = pow(1.0 - max(0.0, dot(V, N)), 3.0)

        # 환경에서 반사 샘플
        env_b = env_sample(Rn)

        # 스페큘러
        spec_angle = max(0.0, dot(Rn, LIGHT_DIR))
        spec = SPEC_STRENGTH * (spec_angle ** SPEC_POWER)

        # 전체 밝기 결합 (0..1)
        brightness = 0.0
        # 유리: 기본적으로 반사(Env) + 미약한 diffuse, 프레넬로 엣지에서 반사 강조
        brightness = 0.7 * env_b + 0.25 * diffuse * (1.0 - fresnel) + 0.9 * fresnel * env_b
        brightness = min(1.0, brightness + spec)

        # 그라데이션 문자 선택
        idx = int(brightness * (len(GRADIENT)-1))
        ch = GRADIENT[max(0, min(len(GRADIENT)-1, idx))]

        # 깊이 비교
        if zcam > depth[py][px]:
            screen[py][px] = ch
            depth[py][px] = zcam

    # 2) 엣지: 굵게, 엣지는 어둡게 커팅된 내부보다 밝게 보이도록
    for e in edges:
        a = vertices[e[0]]; b = vertices[e[1]]
        steps = max(6, int(math.hypot(b[0]-a[0], b[1]-a[1], b[2]-a[2]) * SUBDIV))
        for (x,y,z) in interpolate(a,b,steps):
            xr, yr, zr = rotate(x,y,z, rx, ry, rz)
            cx, cy, zcam = project(xr, yr, zr, width, height)
            if not (0 <= cx < width and 0 <= cy < height): continue

            R = EDGE_THICKNESS
            for dy in range(-R, R+1):
                py = cy + dy
                if not (0 <= py < height): continue
                maxdx = int((R*R - dy*dy)**0.5) if R*R - dy*dy >= 0 else 0
                for dx in range(-maxdx, maxdx+1):
                    px = cx + dx
                    if not (0 <= px < width): continue
                    # 엣지 깊이 우선: 엣지가 더 앞에 보이도록 우선권을 줌
                    if zcam + 0.0001 > depth[py][px]:
                        screen[py][px] = EDGE_CHAR
                        depth[py][px] = zcam + 0.0001

    # 3) 꼭짓점 반짝임: 스페큘러에 의해 반짝이게
    t = time.time()
    for i, v in enumerate(vertices):
        x,y,z = v
        xr, yr, zr = rotate(x,y,z, rx, ry, rz)
        px, py, zcam = project(xr, yr, zr, width, height)
        if not (0 <= px < width and 0 <= py < height): continue
        # 꼭짓점의 프레넬 + 스페큘러 결합
        V = norm((-xr, -yr, -zr))
        # 법선은 꼭짓점이므로 근사로 (sign of coords)
        Nx = math.copysign(1, x); Ny = math.copysign(1, y); Nz = math.copysign(1, z)
        N = (Nx, Ny, Nz)
        fres = pow(1.0 - max(0.0, dot(V, N)), 2.0)
        R = reflect(V, N); Rn = norm(R)
        spec_angle = max(0.0, dot(Rn, LIGHT_DIR))
        spec = SPEC_STRENGTH * (spec_angle ** (SPEC_POWER/2.0))
        blink = fres * 0.6 + 0.4 * spec
        if blink > 0.6:
            ch = VERTEX_CHAR
        else:
            idx = int(max(0, min(len(GRADIENT)-1, int(blink * (len(GRADIENT)-1)))))
            ch = GRADIENT[idx]
        screen[py][px] = ch
        depth[py][px] = zcam + 0.0002

    return "\n".join("".join(row) for row in screen)

# 메인
if __name__ == "__main__":
    try:
        width, height = term_size()
        vertices = make_vertices(SIZE)
        fill_points = sample_cube_surfaces(SIZE, SUBDIV)
        rx = ry = rz = 0.0
        vrx, vry, vrz = 0.058, 0.034, 0.018
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            frame = draw_frame(vertices, EDGES, fill_points, rx, ry, rz, width, height)
            print(frame)
            rx += vrx; ry += vry; rz += vrz
            time.sleep(1.0 / FPS)
    except KeyboardInterrupt:
        sys.exit(0)


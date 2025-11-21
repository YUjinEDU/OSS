import math
import time
import os
import sys
import random

# Windows 환경에서 msvcrt 사용
if os.name == 'nt':
    import msvcrt
else:
    # 다른 OS 지원은 생략 (사용자 환경에 맞춤)
    pass

# ANSI 색상 코드
RESET = "\033[0m"
def color_code(code):
    return f"\033[38;5;{code}m"

# 색상 매핑 (ANSI 256 color)
COLORS = {
    'W': 231, # White
    'Y': 226, # Yellow
    'G': 46,  # Green
    'B': 21,  # Blue
    'R': 196, # Red
    'O': 208  # Orange
}

class Cubie:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        # 각 면의 법선 벡터와 색상
        self.faces = []
        
        # 초기 상태에서 각 방향에 대한 색상 할당
        if y == 1: self.faces.append({'norm': [0, 1, 0], 'color': 'W'})
        if y == -1: self.faces.append({'norm': [0, -1, 0], 'color': 'Y'})
        if x == 1: self.faces.append({'norm': [1, 0, 0], 'color': 'R'})
        if x == -1: self.faces.append({'norm': [-1, 0, 0], 'color': 'O'})
        if z == 1: self.faces.append({'norm': [0, 0, 1], 'color': 'B'})
        if z == -1: self.faces.append({'norm': [0, 0, -1], 'color': 'G'})

    def rotate(self, axis, direction):
        # 90도 회전 (direction: 1 or -1)
        # 회전 행렬 적용
        # x, y, z 축 회전
        x, y, z = self.pos
        nx, ny, nz = x, y, z
        
        if axis == 'x':
            ny = y * 0 - z * direction
            nz = y * direction + z * 0
        elif axis == 'y':
            nx = x * 0 + z * direction
            nz = -x * direction + z * 0
        elif axis == 'z':
            nx = x * 0 - y * direction
            ny = x * direction + y * 0
            
        self.pos = [nx, ny, nz]
        
        # 법선 벡터도 회전
        for face in self.faces:
            fx, fy, fz = face['norm']
            nfx, nfy, nfz = fx, fy, fz
            if axis == 'x':
                nfy = fy * 0 - fz * direction
                nfz = fy * direction + fz * 0
            elif axis == 'y':
                nfx = fx * 0 + fz * direction
                nfz = -fx * direction + fz * 0
            elif axis == 'z':
                nfx = fx * 0 - fy * direction
                nfy = fx * direction + fy * 0
            face['norm'] = [nfx, nfy, nfz]

class RubiksCube:
    def __init__(self):
        self.cubies = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    self.cubies.append(Cubie(x, y, z))
        
        self.rot_x = -0.5
        self.rot_y = 0.5
        self.rot_z = 0.0
        
    def rotate_layer(self, face_code):
        # U, D, L, R, F, B (대문자 시계, 소문자 반시계)
        upper = face_code.upper()
        direction = -1 if face_code.isupper() else 1
        
        # 축과 레이어 정의
        # 좌표계: X(Right), Y(Up), Z(Back)
        # U: Y=1, D: Y=-1
        # R: X=1, L: X=-1
        # B: Z=1, F: Z=-1
        
        axis = ''
        layer = 0
        
        # 회전 방향 보정 (오른손 법칙 기준)
        # U (Y축): 위에서 볼 때 시계방향 -> Y축 기준 음의 회전
        
        if upper == 'U': axis, layer, rot_dir = 'y', 1, -1
        elif upper == 'D': axis, layer, rot_dir = 'y', -1, 1
        elif upper == 'R': axis, layer, rot_dir = 'x', 1, -1
        elif upper == 'L': axis, layer, rot_dir = 'x', -1, 1
        elif upper == 'B': axis, layer, rot_dir = 'z', 1, -1
        elif upper == 'F': axis, layer, rot_dir = 'z', -1, 1
        else: return

        if face_code.islower():
            rot_dir *= -1
            
        for cubie in self.cubies:
            # 부동소수점 오차 고려하여 반올림 비교
            cx, cy, cz = cubie.pos
            val = 0
            if axis == 'x': val = cx
            elif axis == 'y': val = cy
            elif axis == 'z': val = cz
            
            if abs(val - layer) < 0.1:
                cubie.rotate(axis, rot_dir)

    def shuffle(self):
        moves = list("UDLRFB")
        for _ in range(20):
            m = random.choice(moves)
            if random.random() > 0.5: m = m.lower()
            self.rotate_layer(m)

def render(cube, width=80, height=40):
    # Z-buffer 및 문자 버퍼 초기화
    z_buffer = [-9999] * (width * height)
    buffer = [' '] * (width * height)
    
    # 회전 행렬 계산
    cx, sx = math.cos(cube.rot_x), math.sin(cube.rot_x)
    cy, sy = math.cos(cube.rot_y), math.sin(cube.rot_y)
    
    # 각 Cubie 렌더링
    for cubie in cube.cubies:
        x, y, z = cubie.pos
        
        # Cubie 중심 회전
        # Y축 회전
        rx = x * cy + z * sy
        rz = -x * sy + z * cy
        ry = y
        
        # X축 회전
        y2 = ry * cx - rz * sx
        z2 = ry * sx + rz * cx
        x2 = rx
        
        # 각 면 그리기
        for face in cubie.faces:
            fnx, fny, fnz = face['norm']
            
            # 법선 벡터 회전
            nrx = fnx * cy + fnz * sy
            nrz = -fnx * sy + fnz * cy
            nry = fny
            
            ny2 = nry * cx - nrz * sx
            nz2 = nry * sx + nrz * cx
            nx2 = nrx
            
            # Back-face culling (법선이 카메라를 향하는지 확인)
            # 카메라는 -Z 방향에 있다고 가정 (또는 뷰 벡터가 (0,0,-1))
            if nz2 > 0: # 법선이 화면 쪽을 향하면 그림 (간단화)
                continue

            # 면의 중심점 계산 (Cubie 중심 + 법선 * 0.5)
            # 약간의 간격을 위해 0.5 대신 0.52 사용
            fx = x + fnx * 0.52
            fy = y + fny * 0.52
            fz = z + fnz * 0.52
            
            # 면 중심 회전
            frx = fx * cy + fz * sy
            frz = -fx * sy + fz * cy
            fry = fy
            
            fy2 = fry * cx - frz * sx
            fz2 = fry * sx + frz * cx
            fx2 = frx
            
            # 투영
            scale = 30
            dist = 4
            if dist + fz2 == 0: continue
            xp = int(width / 2 + (fx2 * scale) / (dist + fz2) * 2) # *2 for aspect ratio correction
            yp = int(height / 2 - (fy2 * scale) / (dist + fz2))
            
            # 점 하나만 찍는 대신, 면을 채워야 함.
            # 하지만 터미널에서 면 채우기는 복잡하므로, 
            # 각 면을 3x3 점으로 구성하여 그림.
            
            # 면의 기저 벡터 계산 (법선에 수직인 두 벡터)
            # 간단히: 법선이 x축이면 y, z가 기저.
            # 회전된 법선(nx2, ny2, nz2)을 기준으로 접평면 생성
            
            # 더 쉬운 방법:
            # 그냥 큐브 표면에 점을 많이 찍는다.
            # 각 면당 점의 개수를 늘려 면이 꽉 차 보이게 함
            
            base_points = []
            # -0.45 ~ 0.45 범위에서 촘촘하게 점 생성
            steps = [-0.4, -0.2, 0, 0.2, 0.4]
            for u in steps:
                for v in steps:
                    base_points.append((u, v))
            
            for b_u, b_v in base_points:
                # 로컬 좌표에서 월드 좌표로 변환
                # 법선에 따라 u, v가 매핑되는 축이 다름
                px, py, pz = x, y, z
                if abs(fnx) > 0.9: # X면
                    px += fnx * 0.5
                    py += b_u
                    pz += b_v
                elif abs(fny) > 0.9: # Y면
                    px += b_u
                    py += fny * 0.5
                    pz += b_v
                else: # Z면
                    px += b_u
                    py += b_v
                    pz += fnz * 0.5
                
                # 점 회전
                prx = px * cy + pz * sy
                prz = -px * sy + pz * cy
                pry = py
                
                py2 = pry * cx - prz * sx
                pz2 = pry * sx + prz * cx
                px2 = prx
                
                # 투영
                if dist + pz2 <= 0.1: continue
                ooz = 1 / (dist + pz2)
                screen_x = int(width / 2 + (px2 * scale * ooz) * 2)
                screen_y = int(height / 2 - (py2 * scale * ooz))
                
                if 0 <= screen_x < width and 0 <= screen_y < height:
                    idx = screen_y * width + screen_x
                    if ooz > z_buffer[idx]:
                        z_buffer[idx] = ooz
                        char = '#' # or '■'
                        buffer[idx] = color_code(COLORS[face['color']]) + char + RESET

    # 버퍼를 줄 단위로 나누어 문자열로 결합
    lines = []
    for h in range(height):
        lines.append("".join(buffer[h * width : (h + 1) * width]))
    return "\n".join(lines)

def main():
    # Windows ANSI 지원 활성화
    if os.name == 'nt':
        os.system('')
        
    cube = RubiksCube()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Rubik's Cube Simulator")
    print("Controls:")
    print("  Arrow Keys: Rotate View")
    print("  Faces: U, D, F, B, L, R (Shift for inverse)")
    print("  Space: Shuffle")
    print("  Q: Quit")
    print("Press any key to start...")
    if os.name == 'nt': msvcrt.getch()
    
    last_time = time.time()
    
    while True:
        # Input handling
        if os.name == 'nt' and msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\xe0': # Arrow keys
                key = msvcrt.getch()
                if key == b'H': cube.rot_x -= 0.1 # Up
                elif key == b'P': cube.rot_x += 0.1 # Down
                elif key == b'K': cube.rot_y -= 0.1 # Left
                elif key == b'M': cube.rot_y += 0.1 # Right
            else:
                try:
                    char = key.decode('utf-8')
                    if char.lower() == 'q': break
                    if char == ' ': cube.shuffle()
                    if char.upper() in "UDLRFB":
                        cube.rotate_layer(char)
                except:
                    pass
        
        # Render
        output = render(cube)
        
        # Double buffering output
        sys.stdout.write("\033[H" + output)
        sys.stdout.flush()
        
        time.sleep(0.05)

if __name__ == "__main__":
    main()

[33mcommit 12a7c8dcb134f484dab1646b2e4e87d7ebc92747[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mmaster[m[33m)[m
Author: “YUjinEDU” <20191906@edu.hanbat.ac.kr>
Date:   Fri Oct 10 16:02:23 2025 +0900

    2commit

[1mdiff --git a/test.txt b/test.txt[m
[1mindex f8ad089..a59df78 100644[m
[1m--- a/test.txt[m
[1m+++ b/test.txt[m
[36m@@ -1,3 +1,8 @@[m
[32m+[m
[32m+[m[32mthis is eqkrmqekemfkm[m
[32m+[m
[32m+[m
[32m+[m
 ✅ VMware Workstation에서 **Host ↔ Ubuntu(Guest)** 간 복사/붙여넣기 공유를 설정하려면 아래 단계를 따르면 돼요.[m
 (이건 VMware Tools 또는 Open VM Tools 설치가 필요해요.)[m
 [m

[33mcommit 8c73cd72cfcd43ec1725a631b3b2ec82f118eb0f[m
Author: “YUjinEDU” <20191906@edu.hanbat.ac.kr>
Date:   Fri Oct 10 16:01:21 2025 +0900

    first commit

[1mdiff --git a/test.txt b/test.txt[m
[1mnew file mode 100644[m
[1mindex 0000000..f8ad089[m
[1m--- /dev/null[m
[1m+++ b/test.txt[m
[36m@@ -0,0 +1,75 @@[m
[32m+[m[32m✅ VMware Workstation에서 **Host ↔ Ubuntu(Guest)** 간 복사/붙여넣기 공유를 설정하려면 아래 단계를 따르면 돼요.[m
[32m+[m[32m(이건 VMware Tools 또는 Open VM Tools 설치가 필요해요.)[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32m### 🧩 1. VMware 설정 확인[m
[32m+[m
[32m+[m[32m1. VMware 메뉴에서[m
[32m+[m[32m   **Player → Manage → Virtual Machine Settings** 열기[m
[32m+[m[32m2. **Options 탭 → Guest Isolation** 선택[m
[32m+[m[32m3. 다음 두 항목을 모두 체크:[m
[32m+[m
[32m+[m[32m   * ✅ *Enable copy and paste*[m
[32m+[m[32m   * ✅ *Enable drag and drop*[m
[32m+[m[32m4. **OK** 눌러 저장[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32m### 🧰 2. Ubuntu 안에서 VMware Tools 설치[m
[32m+[m
[32m+[m[32mUbuntu 터미널에서 다음 명령을 실행하세요:[m
[32m+[m
[32m+[m[32m```bash[m
[32m+[m[32msudo apt update[m
[32m+[m[32msudo apt install open-vm-tools open-vm-tools-desktop -y[m
[32m+[m[32m```[m
[32m+[m
[32m+[m[32m이후 재부팅:[m
[32m+[m
[32m+[m[32m```bash[m
[32m+[m[32msudo reboot[m
[32m+[m[32m```[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32m### 🧠 3. 재부팅 후 테스트[m
[32m+[m
[32m+[m[32m재부팅이 끝나면[m
[32m+[m
[32m+[m[32m* Host PC → Ubuntu 터미널 또는 텍스트 파일로 복사/붙여넣기[m
[32m+[m[32m* Ubuntu → Host PC 로 복사/붙여넣기[m
[32m+[m
[32m+[m[32m양방향이 정상적으로 작동하는지 확인합니다.[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32m### 🧩 4. 안 될 경우 점검[m
[32m+[m
[32m+[m[32m* VMware Player가 최신 버전인지 확인[m
[32m+[m[32m* Ubuntu GUI (GNOME, Xfce 등)가 정상 동작 중인지 확인[m
[32m+[m[32m* `open-vm-tools`가 백그라운드에서 실행 중인지:[m
[32m+[m
[32m+[m[32m  ```bash[m
[32m+[m[32m  systemctl status vmtoolsd[m
[32m+[m[32m  ```[m
[32m+[m
[32m+[m[32m  “active (running)” 상태여야 정상입니다.[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32m복사 붙여넣기 외에 **파일 드래그 앤 드롭**도 같은 설정으로 가능합니다.[m
[32m+[m[32m만약 여전히 안 된다면 `vmtoolsd` 서비스가 비활성화됐을 가능성이 있으니 다시 시작해보세요:[m
[32m+[m
[32m+[m[32m```bash[m
[32m+[m[32msudo systemctl restart vmtoolsd[m
[32m+[m[32m```[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32m**Q1.** `open-vm-tools` 대신 VMware Tools를 수동으로 설치하면 어떤 차이가 있나요?[m
[32m+[m
[32m+[m[32m**Q2.** 복사/붙여넣기가 안 될 때 `vmware-user` 프로세스가 왜 중요한가요?[m
[32m+[m
[32m+[m[32m**Q3.** 만약 Ubuntu가 최소 GUI 환경일 때 (예: i3, LXDE), 복사 공유를 가능하게 하려면 어떤 추가 설정이 필요할까요?[m
[32m+[m

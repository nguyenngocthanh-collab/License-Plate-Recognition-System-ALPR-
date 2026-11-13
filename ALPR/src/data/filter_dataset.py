from pathlib import Path

raw_path    = Path("./datasets/raw/Vietnamese-license-plate.v6i.yolov8/test/labels")
result_path = Path("./datasets/processed/test/labels")
result_path.mkdir(parents=True, exist_ok=True)   # tạo thư mục nếu chưa có

NEW_CLASS_ID = 0        # label mới thay cho 33
OLD_CLASS_ID = 33

so_file = 0
for file in raw_path.glob("*.txt"):
    # Đọc + ép kiểu
    labels = [
        [int(p[0])] + [float(x) for x in p[1:]]
        for p in (
            line.split()
            for line in file.read_text(encoding='utf-8').splitlines()
            if line.strip()
        )
    ]

    # Lấy dòng đầu tiên có ID lớp == 33
    dong_33 = next((label for label in labels if label[0] == OLD_CLASS_ID), None)

    if dong_33 is None:
        print(f"{file.name}: không có dòng lớp 33 → bỏ qua")
        continue

    # Mod lại label: 33 → 0
    dong_33[0] = NEW_CLASS_ID

    # Ghi ra file cùng tên trong result_path, chỉ chứa dòng đã mod
    noi_dung = " ".join(str(x) for x in dong_33)
    (result_path / file.name).write_text(noi_dung, encoding='utf-8')

    so_file += 1
    print(f"{file.name} → {noi_dung}")

print(f"\nĐã ghi {so_file} file vào {result_path}")
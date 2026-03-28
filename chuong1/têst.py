import requests

# (1) Khai báo headers giả lập trình duyệt Chrome
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# (2) Gửi request GET
url = "https://vnexpress.net/so-hoa/tri-tue-nhan-tao"
response = requests.get(url, headers=headers)

# (3) Kiểm tra mã trạng thái
if response.status_code == 200:
    print(f"Kết nối thành công! Mã trạng thái: {response.status_code}")
else:
    print(f"Kết nối thất bại! Mã trạng thái: {response.status_code}")

# (4) Lưu nội dung HTML vào file
with open("vnexpress_data.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Đã lưu nội dung vào file vnexpress_data.html")

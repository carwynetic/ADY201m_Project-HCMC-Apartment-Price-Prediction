# ADY304m_Project-HCMC-Apartment-Price-Prediction
# 🏙️ HCMC Apartment Price Prediction (Dự đoán giá căn hộ tại TP.HCM)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange.svg)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Latest-green.svg)](https://xgboost.readthedocs.io/)
[![Selenium](https://img.shields.io/badge/Selenium-Web%20Scraping-yellow.svg)](https://www.selenium.dev/)

Đây là kho mã nguồn chính thức của đồ án **"Phân tích và dự đoán đơn giá căn hộ tại TP.HCM bằng các mô hình học máy"**. Dự án xây dựng một đường ống dữ liệu (Data Pipeline) hoàn chỉnh từ khâu thu thập dữ liệu tự động (Web Scraping), tiền xử lý, phân tích khám phá (EDA) đến huấn luyện và đánh giá mô hình học máy.

---

## 🎯 Mục tiêu dự án
* Thu thập và làm sạch dữ liệu thực tế từ thị trường bất động sản trực tuyến (Batdongsan.com.vn).
* Phân tích các yếu tố ảnh hưởng đến đơn giá căn hộ tại TP.HCM (vị trí, diện tích, nội thất).
* Đánh giá và so sánh 10 thuật toán học máy (Linear Models, KNN, SVM, Tree-based Ensembles).
* Xây dựng mô hình dự báo tối ưu và giải thích mức độ đóng góp của từng đặc trưng (Feature Importance).

---

## 📂 Cấu trúc Kho lưu trữ (Repository Structure)

Dự án được tổ chức theo tiêu chuẩn khoa học dữ liệu hiện đại:

```text
ADY304m_Project_HCMC_Apartment/
│
├── data/                           # Chứa dữ liệu qua các giai đoạn
│   ├── raw.csv                     # Dữ liệu cào thô ban đầu
│   ├── stage1_clean_full.csv       # Dữ liệu sau tiền xử lý bằng Python
│   └── stage2_final.csv            # Dữ liệu sạch 100% (16,520 mẫu) để train
│
├── scripts/                        # Mã nguồn Python cốt lõi
│   ├── 01_scraper.py               # Thu thập dữ liệu bằng Selenium/undetected_chromedriver
│   ├── 02_data_cleaning.py         # Làm sạch, Parse dữ liệu, Regex nội thất
│   ├── 03_eda_analysis.py          # Phân tích khám phá (Phân phối, Heatmap, VIF)
│   ├── 04_model_training.py        # Pipeline huấn luyện & so sánh 10 mô hình
│   └── 05_permutation_importance.py# Đánh giá tầm quan trọng đặc trưng (Best Model)
│
├── sql/                            # Mã nguồn truy vấn cơ sở dữ liệu
│   └── 01_outlier_removal.sql      # Lọc ngoại lai theo ngưỡng kinh nghiệm (Domain-based)
│
├── dashboards/                     # Ứng dụng trực quan hóa
│   └── app.py                      # Dashboard phân tích thị trường
│
├── requirements.txt                # Danh sách thư viện Python
├── .gitignore                      # Cấu hình bỏ qua file rác sinh ra lúc chạy code
└── README.md                       # Tài liệu dự án

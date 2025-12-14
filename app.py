# app.py

from flask import Flask, render_template

# Khởi tạo ứng dụng Flask
app = Flask(__name__)


# Định nghĩa đường dẫn trang chủ (root URL '/')
@app.route("/")
def home():
    """Render trang web chính chứa chatbot."""
    # Flask sẽ tìm file 'index.html' trong thư mục 'templates'
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

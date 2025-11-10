from flask import Flask, request, jsonify

app = Flask(__name__)

# Data contoh (anggap seperti database sementara)
data = [
    {"id": 1, "nama": "Agun Nadini", "universitas": "Universitas Nahdlatul Ulama Indonesia"},
    {"id": 2, "nama": "Budi Santoso", "universitas": "Universitas Indonesia"},
    {"id": 3, "nama": "Citra Lestari", "universitas": "Universitas Gadjah Mada"}
]

# Endpoint utama
@app.route('/', methods=['GET', 'POST', 'DELETE'])
def home():
    if request.method == 'GET':
        return '👋 Halo, perkenalkan nama saya Agun Nadini, Mahasiswa semester 5 Universitas Nahdlatul Ulama Indonesia 🚀'
    
    elif request.method == 'POST':
        return jsonify({"message": "POST diterima! Terima kasih telah mengirim data 🙌"})
    
    elif request.method == 'DELETE':
        return jsonify({"message": "Semua data berhasil dihapus (contoh simulasi) 🗑️"})

# Endpoint untuk melihat semua data
@app.route('/data', methods=['GET'])
def get_all_data():
    return jsonify(data)

# Endpoint untuk melihat detail berdasarkan ID
@app.route('/detail/<int:id>', methods=['GET'])
def get_detail(id):
    item = next((d for d in data if d["id"] == id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Data tidak ditemukan"}), 404

# Menjalankan server Flask
if __name__ == '__main__':
    app.run(debug=True)

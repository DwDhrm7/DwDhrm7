#include <iostream>

using namespace std;


double hitung(int lantai, double luas, int kerja){
    double biaya;

    if(lantai == 1){
        biaya = 1000 * luas;
    }else if(lantai == 2){
        biaya = 1500 * luas;
    }else{
        cout<< "Jumlah lantai tidak sesuai." <<endl;
        return 0;
    }

    double tambahan;
    if (kerja == 1){ 
        tambahan = 0.1 * biaya;
    }else if(kerja == 2){ 
        tambahan = 0.05 * biaya;
    }else{
        cout<< "Jenis pekerjaan tidak sesuai." <<endl;
        return 0;
    }

    double TukangUtama = 0.3 * biaya;
    double PembantuTukang = 0.2 * biaya;

    double keuntungan = biaya + tambahan - TukangUtama - PembantuTukang;

    return keuntungan;
}

int main() {
    int lantai, kerja;
    double luas;

    cout << "Jumlah Lantai , Ketik 1 Jika lantai 1;Ketik 2 jika lantai 2 : ";
    cin >> lantai;

    cout << "Luas Bangunan dalam m2 : ";
    cin >> luas;

    cout << "Jenis Pekerjaan, Ketik 1 jika borongan; Ketik 2 jika harian : ";
    cin >> kerja;

    
    double keuntungan = hitung(lantai, luas, kerja);

    cout<< "=============================="<<endl;
    cout<< "Keuntungan proyek anda sebesar " << keuntungan <<endl;
    cout<< " Terimakasih telah menggunakan jasa kami"<<endl;

    return 0;
}


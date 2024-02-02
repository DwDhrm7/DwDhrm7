#include <iostream>
using namespace std;

int main(){
	cout<< " UTS ALGORITMA STRUKTUR DATA "<<"\n";
	cout<< " =========================== "<<"\n";
	
	int hargaL = 5000000;
	int hargaHp = 2500000;
	int hargaHs = 500000;
	int totalBelanja;
	int jumlahL = 0;
	int jumlahHp = 0;
	int jumlahHs = 0;
	
	cout<< " Berapa laptop yang ingin kamu beli : "<<"\n"<<endl;
	cin>> jumlahL;
	
	cout<< " Berapa Smartphone yang ingin kamu beli : "<<"\n"<<endl;
	cin>> jumlahHp;
	
	cout<< " Berapa Headset yang ingin kamu beli : "<<"\n"<<endl;
	cin>> jumlahHs;
	
	totalBelanja = (hargaL * jumlahL) + (hargaHp * jumlahHp) + (hargaHs * jumlahHs);
	cout<< " =========================== "<<"\n";
	int disc = 0;
	if (totalBelanja > 500000){
		int disc = 0.1 * totalBelanja;
		totalBelanja = totalBelanja - disc;
		cout<< " Selamat anda mendapatkan diskon 10% "<<endl;
		cout<< " Diskonnya sebesar : "<<disc<<endl;
	}
	if (totalBelanja > 0){
        cout<< " Harga yang harus anda bayar adalah "<<" Rp "<<totalBelanja<<endl;
    } 
	else{
        cout<< " Anda tidak membeli apapun. "<<endl;
    }
	return 0;
}	
	



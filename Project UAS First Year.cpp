//Pada program ini user memasukkan jumlah elemen array secara dinamis, mengurutkannya dari yang terkecil ke terbesar dan menghitung banyak elemen yang kurang dari 100, menampilkan elemen-elemen apa saja  yang kurang dari 100 dan menampilkan nilai rata rata dari array tersebut.

#include <iostream>
using namespace std;

int perhitungan(int* arr, int n){
    int banyakArray = 0;
    for (int i = 0; i < n; i++){
        if (arr[i] < 100)
	{
            banyakArray++;
        }
    }
    return banyakArray;
}

void tampilkanRataRata(int* arr, int n){
    int total = 0;
    for (int i = 0; i < n; i++){
        total += arr[i];
    }

    if (n > 0)
    {
        double rataRata = static_cast<double>(total) / n;
        cout << "Rata-rata array: " << rataRata << endl;
    }
     else 
    {
        cout << "Array kosong, tidak bisa menampilkan." << endl;
    }
}

void urut(int* arr, int n){
    for (int i = 0; i < n - 1; ++i){
        for (int j = 0; j < n - i - 1; ++j){
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main(){
    int n;
    cout << "Masukkan jumlah array: ";
    cin >> n;

    int* a = new int[n];
    cout << "Masukkan " << n << " Array :\n";
    for (int i = 0; i < n; i++){
        cout << "Array ke-" << i + 1 << ": ";
        cin >> a[i];
    }

    cout << "Nilai array sebelum diurutkan: ";
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;

    urut(a, n);

    cout << "Nilai array setelah diurutkan dari terkecil ke terbesar: ";
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;


    int banyak = perhitungan(a, n);

    cout << "Banyak nilai yang kurang dari 100 sebanyak " << banyak << endl;

    cout << "Nilai nilai yang kurang dari 100: ";
    for (int i = 0; i < n; i++){
        if (a[i] < 100)
	{
            cout << a[i] << " ";
        }
    }

    cout << endl;

    tampilkanRataRata(a, n);

    delete[] a;

    return 0;
}

#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int nilai[5];
    int lulus = 0;
    for (int i = 0; i < 5; ++i) {
        cout << "Masukkan nilai ujian ke " << i + 1 << ": ";
        cin >> nilai[i];

        if (nilai[i] >= 75) {
            lulus++;
        }
         cout<<"------------------------------"<<endl;
    }
    cout<<"=============================="<<endl;
	cout << setw(15) <<right;
    if (lulus == 5) {
        cout << "BAIK SEKALI" <<endl;
    } else if (lulus == 4) {
        cout << "BAIK" <<endl;
    } else if (lulus == 3) {
        cout << "CUKUP" <<endl;
    } else if (lulus == 2) {
        cout << "KURANG" <<endl;
    } else {
        cout << "BURUK" << endl;
    }
    cout<<"==============================" <<endl;
    return 0;
}

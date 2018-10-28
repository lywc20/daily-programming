#include <iostream>
using namespace std;
char l[15];
int lcs_length(char *a, char *b){
    int m =3, n = 5; //toy(3) story(5)
    for(int i = m; i >= 0; i--){
        for(int j = n; j >= 0; j--){
            if(a[i] == '\0' || b[j] == '\0') l[i,j] = 0;
            else if(a[i] == b[j]) l[i,j] = 1 + l[i+1,j+1];
            else l[i,j] = max(l[i+1,j],l[i,j+1]);
        }
    }
    return l[0,0];
}

int main(){
    char a[] = "toy", b[]="story";
    cout << "The longest common subsequence is " << lcs_length(a,b) << endl;
    return 0;
}

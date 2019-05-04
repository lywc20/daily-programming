#include <iostream>
#include <string>
using namespace std;
int i = 0;
int lcs_length(char *a, char *b){
    cout << "call:" << i << " "<< *a << "," << *b << endl;
    if(*a == '\0' || *b == '\0') return 0;
    else if(*a == *b) return 1 + lcs_length(a+1, b+1);
    else {
        cout << "break\n";
        i++;
    return max(lcs_length(a+1,b),lcs_length(a,b+1));
}
}

int main(){
    char str1[] = "toy", str2[] = "story";
    cout << "The longest common subsequence is " << lcs_length(str1, str2) << endl;
    return 0;
}

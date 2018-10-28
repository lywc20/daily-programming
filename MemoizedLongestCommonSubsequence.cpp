//Worst Case O(mn)
#include <iostream>
using namespace std;

char *a, *b;
char l[100];


int subproblem(int i, int j){
    if(l[i,j] < 0){
        if(a[i] == '\0' || b[i] == '\0') l[i,j] = 0;
        else if(a[i] == b[j]) l[i,j] = 1 + subproblem(i+1, j+1);
        else l[i,j] = max(subproblem(i+1,j),subproblem(i,j+1));
    }
    return l[i,j];
}

int lcs_length(char *aa, char *bb){
    a = aa;
    b = bb;
    for(int i = 0; i <= 100; i++){
        for(int j = 0; j <=100; j++){
            l[i,j] = -1;
        }
    }
    return subproblem(0,0);
}
int main(){
    char a[] = "toy", b[] = "story";
    cout << "The longest common subsequence is " << lcs_length(a,b) << endl;
    return 0;
}

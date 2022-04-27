#include<iostream>
#include<math.h>
using namespace std;
int prime(int num){
    for(int i=2;i<=sqrt(num);i++){
        if(num%i==0){
            continue;;
            
        }
        else{
            return num;
        }
    }
}
int main(){
    int a,b;
    cin>>a,b;
    for(int i=a;i<b;i++){
        cout<<prime(i);
    }
    return 0;
}
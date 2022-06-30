//selection sort in C++

#include <iostream.h>  
  
using namespace std;  
  
void sel(int ar[], int n)  
{  
    int i, j, small;  
      
    for (i = 0; i < n-1; i++)      
    {  
        small = i; 
          
        for (j = i+1; j < n; j++)  
        if (ar[j] < ar[small])  
            small = j;  

    int temp = ar[small];  
    ar[small] = ar[i];  
    ar[i] = temp;  
    }  
}  
  
void priArr(int b[], int n)  
{  
    int i;  
    for (i = 0; i < n; i++)  
        cout<< b[i] <<" ";  
}  
  
int main()  
{  
    int b[] = { 80, 20, 29, 13, 8, 70, 15 };  
    int n = sizeof(b) / sizeof(b[0]);  
    cout<< "Before sorting array elements are - "<<endl;  
    priArr(b, n);  
    sel(b, n);  
    cout<< "\nAfter sorting array elements are - "<<endl;    
    priArr(b, n);  
  
    return 0;  
}    



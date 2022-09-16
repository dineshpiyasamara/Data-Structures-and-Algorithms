#include <bits/stdc++.h>
using namespace std;

// implement bubble sort
void bubbleSort(int arr[], int n)
{
    int i, j;
    for (i = 0; i < n - 1; i++)
        for (j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
}

// print an array
void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main()
{
    int arr[] = {12, 6, 7, 8, 10, 2, 9};
    int N = sizeof(arr) / sizeof(arr[0]);
    cout << "Before sorting : ";
    printArray(arr, N);
    bubbleSort(arr, N);
    cout << "After sorting : ";
    printArray(arr, N);
    return 0;
}
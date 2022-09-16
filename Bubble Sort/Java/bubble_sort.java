class bubble_sort {

    // implement bubble sort
    void bubbleSort(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - i - 1; j++)
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
    }

    // print an array
    void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String args[]) {
        bubble_sort bs = new bubble_sort();
        int arr[] = { 12, 6, 7, 8, 10, 2, 9 };
        System.out.print("Before sorting : ");
        bs.printArray(arr);
        bs.bubbleSort(arr);
        System.out.print("After sorting : ");
        bs.printArray(arr);
    }
}

class LinearSearch {
    public static int search(int arr[], int data) {
        int N = arr.length;
        for (int i = 0; i < N; i++) {
            if (arr[i] == data)
                return i;
        }
        return -1;
    }

    public static void main(String args[]) {
        int arr[] = { 12, 21, 8, 16, 34, 51, 6 };
        int data = 34;

        int result = search(arr, data);
        if (result == -1)
            System.out.print("Element is not found");
        else
            System.out.print("Element is found at index " + result);
    }
}
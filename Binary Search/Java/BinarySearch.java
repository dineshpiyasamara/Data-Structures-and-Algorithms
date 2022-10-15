class BinarySearch {
    int binarySearch(int arr[], int l, int r, int data) {
        if (r >= l) {
            int mid = (l + r) / 2;
            if (arr[mid] == data)
                return mid;
            if (arr[mid] > data)
                return binarySearch(arr, l, mid - 1, data);
            return binarySearch(arr, mid + 1, r, data);
        }
        return -1;
    }

    public static void main(String args[]) {
        BinarySearch bs = new BinarySearch();
        int arr[] = { 6, 8, 12, 16, 21, 34, 51 };
        int n = arr.length;
        int data = 21;
        int result = bs.binarySearch(arr, 0, n - 1, data);
        if (result == -1)
            System.out.println("Element is not found");
        else
            System.out.println("Element found at index " + result);
    }
}

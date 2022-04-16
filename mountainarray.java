public class mountainarray {
    public static boolean validMountainArray(int[] A) {
        int N = A.length;
        int i = 0;

        // walk up
        while (i+1 < N && A[i] < A[i+1])
            i++;

        // peak can't be first or last
        if (i == 0 || i == N-1)
            return false;

        // walk down
        while (i+1 < N && A[i] > A[i+1])
            i++;

        return i == N-1;
    }
    public static void main(String[] args){
        int[] test = {0,2,3,4,5,2,1,0};
        boolean ans;
        ans = validMountainArray(test);
        System.out.println(ans);
    }
}
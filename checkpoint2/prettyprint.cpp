vector<vector<int> > Solution::prettyPrint(int A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    int arraySize = (2*A)-1;
    vector<vector<int>> result (arraySize, vector<int>(arraySize, 0));


    //initial pass of creating the grid, this will get most of the right answers
    for(int i=0; i<A; i++){
        for(int j=0; j<A; j++){
            if(j<=i) result[i][j] = A-j;
            else result[i][j] = A-i;
        }
    }

    for(int i=0; i<A; i++){
        for(int j=arraySize-1; j>=A; j--){
            result[i][j] = result[i][arraySize-1-j];
        }
    }

    for(int i=arraySize-1; i>=A; i--){
        for(int j=0;j<arraySize;j++){
            result[i][j] = result[arraySize-1-i][j];
        }
    }


    return result;
}

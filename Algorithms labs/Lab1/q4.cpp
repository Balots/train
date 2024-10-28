#include <iostream>
#include <fstream>
#include <string>


using namespace std;
void qsortRecursive(int *mas, int size) {
    int i = 0;
    int j = size - 1;
    int mid = mas[size / 2];
    do {
        while(mas[i] < mid) {
            i++;
        }
        while(mas[j] > mid) {
            j--;
        }
        if (i <= j) {
            int tmp = mas[i];
            mas[i] = mas[j];
            mas[j] = tmp;

            i++;
            j--;
        }
    } while (i <= j);
    if(j > 0) {
        qsortRecursive(mas, j + 1);
    }
    if (i < size) {
        qsortRecursive(&mas[i], size - i);
    }
}

int* chartrans(char* sym, int size)
{
    static int res[10000];
    for(int i = 0; i <= size; i++)
    {
        res[i] = (int) sym[i];
    }
    return res;
}

char* inttrans(int* mas, int size)
{
    static char res[10000];
    for(int i = 0; i <= size; i++)
    {
        if(mas[i] != 0)
        {
            res[i] = (char) mas[i];
        }
    }
    return res;
}

int main()
{
    fstream out;
    char line[10000];
    ifstream in("input.txt");
    while(in.getline(line, 10000))
    {
        int size = 100;
        int* arr = chartrans(line, size);
        qsortRecursive(arr, size);
        char* ans = inttrans(arr, size);
        cout.write(ans, 10000);
        cout << endl;
    }

    in.close();
    return 0;
}
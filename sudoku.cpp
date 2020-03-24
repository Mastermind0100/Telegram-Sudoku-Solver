#include <iostream>
#include <fstream>

using namespace std;

bool validity_check(int sudoku[9][9],int n,int p,int q)
{
    for(int i=0;i<9;i++)
    {
        if(sudoku[p][i]==n && q!=i)
        {
            return false;
        }
    }
    for(int i=0;i<9;i++)
    {
        if(sudoku[i][q]==n && p!=i)
        {
            return false;
        }
    }
    int bx=q/3;
    int by=p/3;
    for(int i=by*3;i<by*3+3;i++)
    {
        for(int j=bx*3;j<bx*3+3;j++)
        {
            if(sudoku[i][j]==n && i!=p && j!=q)
            {
                return false;
            }
        }
    }
    return true;
}

int blank(int sudoku[9][9],int *r,int *c)
{
    for(*r=0;*r<9;(*r)++)
    {
        for(*c=0;*c<9;(*c)++)
        {
            if(sudoku[*r][*c]==0)
            {
                return 1;
            }
        }
    }
    return 0;
}

bool solver(int sudoku[9][9])
{
    int row=0,col=0;
    int x=-1,y=-1;

    if (!blank(sudoku, &row, &col)){
		return 1;
	}
    for(int i=1;i<=9;i++)
    {
        if(validity_check(sudoku,i,row,col))
        {
            sudoku[row][col]=i;
            if(solver(sudoku))
            {
                return true;
            }
            sudoku[row][col]=0;
        }
    }
    return false;
}

void print_sudoku(int sudoku[9][9])
{
    for(int i=0;i<9;i++)
    {
        for(int j=0;j<9;j++)
        {
            cout<<sudoku[i][j]<<"  ";
        }
        cout<<endl<<endl;
    }
}

int main()
{
    int x;
    ifstream inFile;
    inFile.open("unsolved.txt");
    // if (!inFile) 
    // {
    // cerr << "Unable to open file datafile.txt";
    // exit(1);   // call system to stop
    // }
    int unsolved_puzzle[81];
    int sudoku[9][9];
    int k = 0;
    while (inFile >> x) 
    {
        unsolved_puzzle[k] = x;           
        k++;
    }
    inFile.close();
    
    int q = 0;
    for(int i=0;i<9;i++)
    {
        for(int j=0;j<9;j++)
        {
            sudoku[i][j] = unsolved_puzzle[q];
            q++;
        }
    }
    
    
    if (solver(sudoku) == true)
    {
        cout<<"-------------------------"<<endl;
        cout<<"         SOLVED!         "<<endl;
        cout<<"-------------------------"<<endl;
        print_sudoku(sudoku);
        fstream new_file;
        new_file.open("solved.txt",ios::out);
        for(int i = 0; i < 9; i++)
        {
            for(int j = 0; j < 9; j++)
            {
                new_file<<sudoku[i][j];
                new_file<<" ";
            }
            new_file<<'\n';
        }
    }
    else
        cout << "Solution Does Not Exist!";
    return 0;
}
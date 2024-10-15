// C++ program for the above approach

#include <bits/stdc++.h>
using namespace std;

// Function to print the pattern of a fish
// over N rows
void printFish(int N)
{

	string spaces1 = "", spaces2 = "";
	string stars1 = "*", stars2 = "";
	for (int i = 0; i < N; ++i) {
		spaces1 += ' ';
	}
	spaces2 = spaces1;

	for (int i = 0; i < 2 * N + 1; ++i) {
		// For upper part
		if (i < N) {
			cout << spaces1 << stars1
				<< spaces1 << spaces1
				<< stars2 << endl;
			spaces1.pop_back();
			stars1 += "**";
			stars2 += "*";
		}

		// For middle part
		if (i == N) {
			cout << spaces1 << stars1
				<< spaces1 << spaces1
				<< stars2 << endl;
		}

		// For lower part
		if (i > N) {
			spaces1 += ' ';
			stars1.pop_back();
			stars1.pop_back();
			stars2.pop_back();
			cout << spaces1 << stars1
				<< spaces1 << spaces1
				<< stars2 << endl;
		}
	}
}

// Driver Code
int main()
{
	int N = 5;
	printFish(N);
}

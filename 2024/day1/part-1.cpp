#include <bits/stdc++.h>

#define NAME "input"
#define i32 int
#define i64 int64_t
#define u32 unsigned int
#define u64 unsigned long long
#define ll long long
#define ld long double
#define ii pair<int, int>
#define vi vector<int>
#define vii vector<vector<int>>
#define vec vector
#define fi first
#define se second
#define sz(a) (u32)(a.size())
#define all(a) a.begin(), a.end()
#define rev(a) a.rbegin(), a.rend()

using namespace std;

const int MOD = 1e9 + 7;
const int N = 1e5 + 5;
const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    freopen(NAME".inp", "r", stdin);
    // freopen(NAME".out", "w", stdout);

    int res = 0;
    vec<int> a, b;
    for (int i = 0; i < 1000; ++i) {
        int x, y;
        cin >> x >> y;
        a.push_back(x);
        b.push_back(y);
    }

    sort(all(a));
    sort(all(b));

    for (int i = 0; i < 1000; ++i) {
        res += abs(a[i] - b[i]);
    }
    cout << res;

    return 0;
}
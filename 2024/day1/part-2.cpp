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

    unordered_map<int, int> cnt;
    vec<int> a;
    for (int i = 0; i < 1000; ++i) {
        int x, y;
        cin >> x >> y;
        cnt[y]++;
        a.push_back(x);
    }

    ll res = 0;
    for (int i = 0; i < 1000; ++i) {
        if (cnt.count(a[i])) res += 1ll * a[i] * cnt[a[i]];
        // cout << a[i] << ' ' << cnt[a[i]] << '\n';
    }
    cout << res;

    return 0;
}
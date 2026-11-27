"""酸洗膏完全反應理論值計算（每 100 kg）。
用法：python3 tools/配方計算.py
假設：Mg 先把氟沉澱成 MgF2；Na、NH4 先配硫酸根（硫酸鈉／硫酸銨，實際在酸中多為硫酸氫鹽）；
其餘硫酸根為硫酸；剩餘氟為游離 HF；Na/NH4 配完硫酸根仍有剩，才配硝酸（硝酸銨）。
"""
def comp(m=0, f=0, a=0, n=0, t=0, hfc=.095, nc=.55, water=0, name=''):
    """m=七水硫酸鎂 f=氟化鈉 a=氟化氫銨 n=硝酸溶液 t=外加增稠劑 water=加水；其餘補氫氟酸溶液"""
    h = 100 - m - f - a - n - t - water
    M = m/246.47; Na = f/41.99; A = a/57.04; N = n*nc/63.01
    F = h*hfc/20.006 + Na + 2*A
    mg = min(M, F/2); Ff = F - 2*mg; Mrest = M - mg; so4 = mg
    C = Na + A
    salt = min(C/2, so4); h2so4 = (so4 - salt)*98.08
    nas = min(Na/2, salt); nh4s = salt - nas
    ex = max(C - 2*so4, 0); nh4no3 = min(ex, N)
    w = water + h*(1-hfc) + n*(1-nc) + M*7*18.015
    print(f'{name}：{hfc*100:g}%氫氟酸 {h:.1f}｜游離HF {Ff*20.006:.2f}% 硝酸 {(N-nh4no3)*63.01:.1f}% 硫酸 {h2so4:.1f}% '
          f'硫酸鈉 {nas*142.04:.1f}% 硫酸銨 {nh4s*132.14:.1f}% 硝酸銨 {nh4no3*80.04:.1f}% 剩硫酸鎂 {Mrest*120.37:.1f}% '
          f'原位氟化鎂 {mg*62.3:.1f}% 外加增稠 {t}% 水 {w:.1f}%')

if __name__ == '__main__':
    comp(m=35, n=30, hfc=.55, water=20, name='原配方')
    comp(m=46.1, f=4.6, n=2.8, name='現行')
    comp(m=20, a=3.4, n=26, t=12, name='E2 硫酸鎂＋硫酸鋇')
    comp(m=12, a=2.4, n=26, t=20, name='E3 少鎂多鋇')
    comp(m=35, a=9, n=26, name='E4 硫酸鎂＋氟化氫銨')
    comp(m=28, a=7, n=26, t=6, name='E5 硫酸鎂＋氟化氫銨＋少量硫酸鋇')

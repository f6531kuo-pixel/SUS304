"""酸洗膏完全反應理論值計算（每 100 kg）。
用法：python3 tools/配方計算.py
假設：Mg 先把氟沉澱成 MgF2；Na 先配硫酸根成 Na2SO4；其餘硫酸根為硫酸；剩餘氟為游離 HF。
"""
def comp(m, f, n, t, hfconc=.095, nconc=.55, total=100, name='', water=0):
    """m=七水硫酸鎂 f=氟化鈉 n=硝酸溶液 t=外加增稠劑（氟化鎂粉或硫酸鋇），其餘補 9.5% 氫氟酸"""
    h = total - m - f - n - t - water
    M = m/246.47; F = h*hfconc/20.006 + f/41.99; Na = f/41.99; N = n*nconc/63.01
    mg = min(M, F/2); Ffree = F - 2*mg; Mrest = M - mg
    so4 = M - Mrest
    h2so4 = max(so4 - Na/2, 0)*98.08; na2so4 = min(Na/2, so4)*142.04
    w = water + h*(1-hfconc) + n*(1-nconc) + M*7*18.015
    print(f'{name}：{hfconc*100:g}%氫氟酸 {h:.1f}｜游離HF {Ffree*20.006:.2f}% 硝酸 {N*63.01:.1f}% 硫酸 {h2so4:.1f}% '
          f'硫酸鈉 {na2so4:.1f}% 剩硫酸鎂 {Mrest*120.37:.1f}% 原位氟化鎂 {mg*62.3:.1f}% 外加增稠 {t}% 水 {w:.1f}%')

if __name__ == '__main__':
    comp(35, 0, 30, 0, hfconc=.55, water=20, name='原配方')
    comp(46.1, 4.6, 2.8, 0, name='現行')
    comp(20, 5, 26, 8, name='E1 硫酸鎂＋氟化鎂粉')
    comp(20, 5, 26, 12, name='E2 硫酸鎂＋硫酸鋇')
    comp(12, 3.5, 26, 20, name='E3 少鎂多鋇')

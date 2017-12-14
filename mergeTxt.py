# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:23:31 2017

@author: jsx
主要功能：
将多个TXT文件合并为一个TXT文件

"""
'''
flist = ['log1.txt','log2.txt','log3.txt','log4.txt','log5.txt',
         'log11.txt','log12.txt','log13.txt','log14.txt','log15.txt',
         'log6.txt','log7.txt','log8.txt','log9.txt','log10.txt',
         'log16.txt','log17.txt','log18.txt','log19.txt','log20.txt',
         'log21.txt','log22.txt','log23.txt','log24.txt','log25.txt',
         'log26.txt','log27.txt','log28.txt','log29.txt','log30.txt',
         'log31.txt','log32.txt','log33.txt','log34.txt','log35.txt',
         'log36.txt','log37.txt','log38.txt','log39.txt','log40.txt',
         'log41.txt','log42.txt','log43.txt','log44.txt','log45.txt',
         'log46.txt','log47.txt','log48.txt','log49.txt','log50.txt',
         'log51.txt','log52.txt','log53.txt','log54.txt','log55.txt',
         'log56.txt','log57.txt','log58.txt','log59.txt','log60.txt',
         'log61.txt','log62.txt','log63.txt','log64.txt','log65.txt',
         'log66.txt','log67.txt','log68.txt','log69.txt','log70.txt',
         'log71.txt','log72.txt','log73.txt','log74.txt','log75.txt',
         'log76.txt','log77.txt','log78.txt','log79.txt','log80.txt',
         'log81.txt','log82.txt','log83.txt','log84.txt','log85.txt',
         'log86.txt','log87.txt','log88.txt','log89.txt','log90.txt',
         'log91.txt','log92.txt','log93.txt','log94.txt','log95.txt',
         'log96.txt','log97.txt','log98.txt','log99.txt','log100.txt']

#flist = ['out_30log.txt','out_130log.txt']

flist = ['tan1.txt','tan2.txt','tan3.txt','tan4.txt','tan5.txt',
         'tan6.txt','tan7.txt','tan8.txt','tan9.txt','tan10.txt',
         'tan11.txt','tan12.txt','tan13.txt','tan14.txt','tan15.txt',
         'tan16.txt','tan17.txt','tan18.txt','tan19.txt','tan20.txt',
         'tan21.txt','tan22.txt','tan23.txt','tan24.txt','tan25.txt',
         'tan26.txt','tan27.txt','tan28.txt','tan29.txt','tan30.txt',
         'tan31.txt','tan32.txt','tan33.txt','tan34.txt','tan35.txt',
         'tan36.txt','tan37.txt','tan38.txt','tan39.txt','tan40.txt',
         'tan41.txt','tan42.txt','tan43.txt','tan44.txt','tan45.txt',
         'tan46.txt','tan47.txt','tan48.txt','tan49.txt','tan50.txt',
         'tan51.txt','tan52.txt','tan53.txt','tan54.txt','tan55.txt',
         'tan56.txt','tan57.txt','tan58.txt','tan59.txt','tan60.txt',
         'tan61.txt','tan62.txt','tan63.txt','tan64.txt','tan65.txt',
         'tan66.txt','tan67.txt','tan68.txt','tan69.txt','tan70.txt',
         'tan71.txt','tan72.txt','tan73.txt','tan74.txt','tan75.txt',
         'tan76.txt','tan77.txt','tan78.txt','tan79.txt','tan80.txt',
         'tan81.txt','tan82.txt','tan83.txt','tan84.txt','tan85.txt',
         'tan86.txt','tan87.txt','tan88.txt','tan89.txt','tan90.txt',
         'tan91.txt','tan92.txt','tan93.txt','tan94.txt','tan95.txt',
         'tan96.txt','tan97.txt','tan98.txt','tan99.txt','tan100.txt']


flist =['sin1.txt','sin2.txt','sin3.txt','sin4.txt','sin5.txt',
        'sin6.txt','sin7.txt','sin8.txt','sin9.txt','sin10.txt',
        'sin11.txt','sin12.txt','sin13.txt','sin14.txt','sin15.txt',
        'sin16.txt','sin17.txt','sin18.txt','sin19.txt','sin20.txt',
        'sin21.txt','sin22.txt','sin23.txt','sin24.txt','sin25.txt',
        'sin26.txt','sin27.txt','sin28.txt','sin29.txt','sin30.txt',
        'sin31.txt','sin32.txt','sin33.txt','sin34.txt','sin35.txt',
        'sin36.txt','sin37.txt','sin38.txt','sin39.txt','sin40.txt',
        'sin41.txt','sin42.txt','sin43.txt','sin44.txt','sin45.txt',
        'sin46.txt','sin47.txt','sin48.txt','sin49.txt','sin50.txt',
        'sin51.txt','sin52.txt','sin53.txt','sin54.txt','sin55.txt',
        'sin56.txt','sin57.txt','sin58.txt','sin59.txt','sin60.txt',
        'sin61.txt','sin62.txt','sin63.txt','sin64.txt','sin65.txt',
        'sin66.txt','sin67.txt','sin68.txt','sin69.txt','sin70.txt',
        'sin71.txt','sin72.txt','sin73.txt','sin74.txt','sin75.txt',
        'sin76.txt','sin77.txt','sin78.txt','sin79.txt','sin80.txt',
        'sin81.txt','sin82.txt','sin83.txt','sin84.txt','sin85.txt',
        'sin86.txt','sin87.txt','sin88.txt','sin89.txt','sin90.txt',
        'sin91.txt','sin92.txt','sin93.txt','sin94.txt','sin95.txt',
        'sin96.txt','sin97.txt','sin98.txt','sin99.txt','sin100.txt']
      
flist = ['13332_201211__40.600000000.txt','13332_201212__38.000000000.txt','13332_201301__38.300000000.txt','13332_201302__37.800000000.txt','13332_201303__38.900000000.txt']

flist =['101.txt','102.txt','103.txt','104.txt','105.txt','106.txt','107.txt','108.txt','109.txt',
        '110.txt','111.txt','112.txt','113.txt','114.txt','115.txt','116.txt','117.txt','118.txt','119.txt',
        '120.txt','121.txt','122.txt','123.txt','124.txt','125.txt','126.txt','127.txt','128.txt','129.txt',
        '130.txt','131.txt','132.txt','133.txt','134.txt','135.txt','136.txt','137.txt','138.txt','139.txt',
        '140.txt','141.txt','142.txt','143.txt','144.txt','145.txt','146.txt','147.txt','148.txt','149.txt',
        '150.txt']

flist = ['13332_201303__38.900000000.txt','13332_201304__41.600000000.txt','13332_201305__37.900000000.txt',
         '13332_201306__42.600000000.txt','13332_201307__39.200000000.txt','13332_201308__41.000000000.txt','13332_201309_39.3000000000.txt']

#emcodng=utf-8
flist = ['3084_201210.txt','3084_201211.txt','3084_201212.txt','3084_201301.txt','3084_201302.txt',
         '3084_201303.txt','3084_201304.txt','3084_201305.txt','3084_201306.txt','3084_201301.txt',
         '3084_201307.txt','3084_201308.txt','3084_201309.txt']
flist = ['13332-5.txt','13332-7.txt']
'''
flist = ['0.txt','1.txt','2.txt','3.txt','4.txt',
         '5.txt','6.txt','7.txt',
         '8.txt','9.txt','10.txt']
outfile = open('test.txt','w')

for fr in flist:
    for txt in open(fr,'r'):
        outfile.write(txt)
outfile.close()

print '合并文件Done!'
        

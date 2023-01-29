import re



    

dic = {re.compile("^a$"):list(map(chr, range(0x12000, 0x12040))),
       re.compile("^b$"):list(map(chr, range(0x12040, 0x12055))),
       re.compile("^d$"):list(map(chr, range(0x12055, 0x1208A))),
       re.compile("^e$"):list(map(chr, range(0x1208A, 0x120B5))),
       re.compile("^g$"):list(map(chr, range(0x120B5, 0x12129))),
       re.compile("^h$"):list(map(chr, range(0x12129, 0x1213F))),
       re.compile("^i$"):list(map(chr, range(0x1213F, 0x12157))),
       re.compile("^k$"):list(map(chr, range(0x12157, 0x121B7))),
       re.compile("^l$"):list(map(chr, range(0x121B7, 0x12220))),
       re.compile("^m$"):list(map(chr, range(0x12220, 0x1223E))),
       re.compile("^n$"):list(map(chr, range(0x1223E, 0x1227A))),
       re.compile("^p$"):list(map(chr, range(0x1227A, 0x1228F))),
       re.compile("^r$"):list(map(chr, range(0x1228F, 0x12293))),
       re.compile("^s$"):list(map(chr, range(0x12293, 0x122EB))),
       re.compile("^t$"):list(map(chr, range(0x122EB, 0x1230B))),
       re.compile("^u$"):list(map(chr, range(0x1230B, 0x1235D))),
       re.compile("^z$"):list(map(chr, range(0x1235D, 0x1236F))),
       re.compile("^q$"):list(map(chr, range(0x12370, 0x12400))),
       re.compile("^1$"):list(map(chr, range(0x12400, 0x12408))),
       re.compile("^2$"):list(map(chr, range(0x12408, 0x1240F))),
       re.compile("^3$"):list(map(chr, range(0x1240F, 0x12415))),
       re.compile("^4$"):list(map(chr, range(0x12415, 0x1241E))),
       re.compile("^5$"):list(map(chr, range(0x1241E, 0x12423))),
       re.compile("^6$"):list(map(chr, range(0x12423, 0x1242C))),
       re.compile("^7$"):list(map(chr, range(0x1242C, 0x12432))),
       re.compile("^8$"):list(map(chr, range(0x12432, 0x12434))),
       re.compile("^9$"):list(map(chr, range(0x12434, 0x1243A))),
       re.compile("^0$"):list(map(chr, range(0x1243A, 0x12442))),
       re.compile("^c$"):list(map(chr, range(0x12442, 0x12444))),
       re.compile("^f$"):list(map(chr, range(0x12444, 0x1244A))),
       re.compile("^j$"):list(map(chr, range(0x1244A, 0x1244F))),
       re.compile("^o$"):list(map(chr, range(0x1244F, 0x12456))),
       re.compile("^v$"):list(map(chr, range(0x12456, 0x12458))),
       re.compile("^x$"):list(map(chr, range(0x12458, 0x1245A))),
       re.compile("^;$"):list(map(chr, range(0x1245A, 0x1245F))),
       re.compile("^:$"):list(map(chr, range(0x1245F, 0x12465))),
       re.compile("^/$"):list(map(chr, range(0x12465, 0x12467))),
       re.compile("^w$"):list(map(chr, range(0x12467, 0x12469))),
       re.compile("^y$"):list(map(chr, range(0x12469, 0x1246F))),
       re.compile("^-$"):list(map(chr, range(0x12470, 0x12475)))}

       
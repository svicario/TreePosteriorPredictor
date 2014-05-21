#Data taken from the code of mrbayes 3.2.2 file model.c
#the order of the aminoacid is the same 
# A R N D C Q E G H I L K M F P S T W Y V */

#jones
aaJones=20*[["0"*20]]
aaJones=[i[0].split("0") for i in aaJones]
aaJones[ 0][ 0] =   0; aaJones[ 0][ 1] =  58; aaJones[ 0][ 2] =  54; aaJones[ 0][ 3] =  81; aaJones[ 0][ 4] =  56; 
aaJones[ 0][ 5] =  57; aaJones[ 0][ 6] = 105; aaJones[ 0][ 7] = 179; aaJones[ 0][ 8] =  27; aaJones[ 0][ 9] =  36; 
aaJones[ 0][10] =  30; aaJones[ 0][11] =  35; aaJones[ 0][12] =  54; aaJones[ 0][13] =  15; aaJones[ 0][14] = 194; 
aaJones[ 0][15] = 378; aaJones[ 0][16] = 475; aaJones[ 0][17] =   9; aaJones[ 0][18] =  11; aaJones[ 0][19] = 298; 
aaJones[ 1][ 0] =  58; aaJones[ 1][ 1] =   0; aaJones[ 1][ 2] =  45; aaJones[ 1][ 3] =  16; aaJones[ 1][ 4] = 113; 
aaJones[ 1][ 5] = 310; aaJones[ 1][ 6] =  29; aaJones[ 1][ 7] = 137; aaJones[ 1][ 8] = 328; aaJones[ 1][ 9] =  22; 
aaJones[ 1][10] =  38; aaJones[ 1][11] = 646; aaJones[ 1][12] =  44; aaJones[ 1][13] =   5; aaJones[ 1][14] =  74; 
aaJones[ 1][15] = 101; aaJones[ 1][16] =  64; aaJones[ 1][17] = 126; aaJones[ 1][18] =  20; aaJones[ 1][19] =  17; 
aaJones[ 2][ 0] =  54; aaJones[ 2][ 1] =  45; aaJones[ 2][ 2] =   0; aaJones[ 2][ 3] = 528; aaJones[ 2][ 4] =  34; 
aaJones[ 2][ 5] =  86; aaJones[ 2][ 6] =  58; aaJones[ 2][ 7] =  81; aaJones[ 2][ 8] = 391; aaJones[ 2][ 9] =  47; 
aaJones[ 2][10] =  12; aaJones[ 2][11] = 263; aaJones[ 2][12] =  30; aaJones[ 2][13] =  10; aaJones[ 2][14] =  15; 
aaJones[ 2][15] = 503; aaJones[ 2][16] = 232; aaJones[ 2][17] =   8; aaJones[ 2][18] =  70; aaJones[ 2][19] =  16; 
aaJones[ 3][ 0] =  81; aaJones[ 3][ 1] =  16; aaJones[ 3][ 2] = 528; aaJones[ 3][ 3] =   0; aaJones[ 3][ 4] =  10; 
aaJones[ 3][ 5] =  49; aaJones[ 3][ 6] = 767; aaJones[ 3][ 7] = 130; aaJones[ 3][ 8] = 112; aaJones[ 3][ 9] =  11; 
aaJones[ 3][10] =   7; aaJones[ 3][11] =  26; aaJones[ 3][12] =  15; aaJones[ 3][13] =   4; aaJones[ 3][14] =  15; 
aaJones[ 3][15] =  59; aaJones[ 3][16] =  38; aaJones[ 3][17] =   4; aaJones[ 3][18] =  46; aaJones[ 3][19] =  31; 
aaJones[ 4][ 0] =  56; aaJones[ 4][ 1] = 113; aaJones[ 4][ 2] =  34; aaJones[ 4][ 3] =  10; aaJones[ 4][ 4] =   0; 
aaJones[ 4][ 5] =   9; aaJones[ 4][ 6] =   5; aaJones[ 4][ 7] =  59; aaJones[ 4][ 8] =  69; aaJones[ 4][ 9] =  17; 
aaJones[ 4][10] =  23; aaJones[ 4][11] =   7; aaJones[ 4][12] =  31; aaJones[ 4][13] =  78; aaJones[ 4][14] =  14; 
aaJones[ 4][15] = 223; aaJones[ 4][16] =  42; aaJones[ 4][17] = 115; aaJones[ 4][18] = 209; aaJones[ 4][19] =  62; 
aaJones[ 5][ 0] =  57; aaJones[ 5][ 1] = 310; aaJones[ 5][ 2] =  86; aaJones[ 5][ 3] =  49; aaJones[ 5][ 4] =   9; 
aaJones[ 5][ 5] =   0; aaJones[ 5][ 6] = 323; aaJones[ 5][ 7] =  26; aaJones[ 5][ 8] = 597; aaJones[ 5][ 9] =   9; 
aaJones[ 5][10] =  72; aaJones[ 5][11] = 292; aaJones[ 5][12] =  43; aaJones[ 5][13] =   4; aaJones[ 5][14] = 164; 
aaJones[ 5][15] =  53; aaJones[ 5][16] =  51; aaJones[ 5][17] =  18; aaJones[ 5][18] =  24; aaJones[ 5][19] =  20; 
aaJones[ 6][ 0] = 105; aaJones[ 6][ 1] =  29; aaJones[ 6][ 2] =  58; aaJones[ 6][ 3] = 767; aaJones[ 6][ 4] =   5; 
aaJones[ 6][ 5] = 323; aaJones[ 6][ 6] =   0; aaJones[ 6][ 7] = 119; aaJones[ 6][ 8] =  26; aaJones[ 6][ 9] =  12; 
aaJones[ 6][10] =   9; aaJones[ 6][11] = 181; aaJones[ 6][12] =  18; aaJones[ 6][13] =   5; aaJones[ 6][14] =  18; 
aaJones[ 6][15] =  30; aaJones[ 6][16] =  32; aaJones[ 6][17] =  10; aaJones[ 6][18] =   7; aaJones[ 6][19] =  45; 
aaJones[ 7][ 0] = 179; aaJones[ 7][ 1] = 137; aaJones[ 7][ 2] =  81; aaJones[ 7][ 3] = 130; aaJones[ 7][ 4] =  59; 
aaJones[ 7][ 5] =  26; aaJones[ 7][ 6] = 119; aaJones[ 7][ 7] =   0; aaJones[ 7][ 8] =  23; aaJones[ 7][ 9] =   6; 
aaJones[ 7][10] =   6; aaJones[ 7][11] =  27; aaJones[ 7][12] =  14; aaJones[ 7][13] =   5; aaJones[ 7][14] =  24; 
aaJones[ 7][15] = 201; aaJones[ 7][16] =  33; aaJones[ 7][17] =  55; aaJones[ 7][18] =   8; aaJones[ 7][19] =  47; 
aaJones[ 8][ 0] =  27; aaJones[ 8][ 1] = 328; aaJones[ 8][ 2] = 391; aaJones[ 8][ 3] = 112; aaJones[ 8][ 4] =  69; 
aaJones[ 8][ 5] = 597; aaJones[ 8][ 6] =  26; aaJones[ 8][ 7] =  23; aaJones[ 8][ 8] =   0; aaJones[ 8][ 9] =  16; 
aaJones[ 8][10] =  56; aaJones[ 8][11] =  45; aaJones[ 8][12] =  33; aaJones[ 8][13] =  40; aaJones[ 8][14] = 115; 
aaJones[ 8][15] =  73; aaJones[ 8][16] =  46; aaJones[ 8][17] =   8; aaJones[ 8][18] = 573; aaJones[ 8][19] =  11; 
aaJones[ 9][ 0] =  36; aaJones[ 9][ 1] =  22; aaJones[ 9][ 2] =  47; aaJones[ 9][ 3] =  11; aaJones[ 9][ 4] =  17; 
aaJones[ 9][ 5] =   9; aaJones[ 9][ 6] =  12; aaJones[ 9][ 7] =   6; aaJones[ 9][ 8] =  16; aaJones[ 9][ 9] =   0; 
aaJones[ 9][10] = 229; aaJones[ 9][11] =  21; aaJones[ 9][12] = 479; aaJones[ 9][13] =  89; aaJones[ 9][14] =  10; 
aaJones[ 9][15] =  40; aaJones[ 9][16] = 245; aaJones[ 9][17] =   9; aaJones[ 9][18] =  32; aaJones[ 9][19] = 961; 
aaJones[10][ 0] =  30; aaJones[10][ 1] =  38; aaJones[10][ 2] =  12; aaJones[10][ 3] =   7; aaJones[10][ 4] =  23; 
aaJones[10][ 5] =  72; aaJones[10][ 6] =   9; aaJones[10][ 7] =   6; aaJones[10][ 8] =  56; aaJones[10][ 9] = 229; 
aaJones[10][10] =   0; aaJones[10][11] =  14; aaJones[10][12] = 388; aaJones[10][13] = 248; aaJones[10][14] = 102; 
aaJones[10][15] =  59; aaJones[10][16] =  25; aaJones[10][17] =  52; aaJones[10][18] =  24; aaJones[10][19] = 180; 
aaJones[11][ 0] =  35; aaJones[11][ 1] = 646; aaJones[11][ 2] = 263; aaJones[11][ 3] =  26; aaJones[11][ 4] =   7; 
aaJones[11][ 5] = 292; aaJones[11][ 6] = 181; aaJones[11][ 7] =  27; aaJones[11][ 8] =  45; aaJones[11][ 9] =  21; 
aaJones[11][10] =  14; aaJones[11][11] =   0; aaJones[11][12] =  65; aaJones[11][13] =   4; aaJones[11][14] =  21; 
aaJones[11][15] =  47; aaJones[11][16] = 103; aaJones[11][17] =  10; aaJones[11][18] =   8; aaJones[11][19] =  14; 
aaJones[12][ 0] =  54; aaJones[12][ 1] =  44; aaJones[12][ 2] =  30; aaJones[12][ 3] =  15; aaJones[12][ 4] =  31; 
aaJones[12][ 5] =  43; aaJones[12][ 6] =  18; aaJones[12][ 7] =  14; aaJones[12][ 8] =  33; aaJones[12][ 9] = 479; 
aaJones[12][10] = 388; aaJones[12][11] =  65; aaJones[12][12] =   0; aaJones[12][13] =  43; aaJones[12][14] =  16; 
aaJones[12][15] =  29; aaJones[12][16] = 226; aaJones[12][17] =  24; aaJones[12][18] =  18; aaJones[12][19] = 323; 
aaJones[13][ 0] =  15; aaJones[13][ 1] =   5; aaJones[13][ 2] =  10; aaJones[13][ 3] =   4; aaJones[13][ 4] =  78; 
aaJones[13][ 5] =   4; aaJones[13][ 6] =   5; aaJones[13][ 7] =   5; aaJones[13][ 8] =  40; aaJones[13][ 9] =  89; 
aaJones[13][10] = 248; aaJones[13][11] =   4; aaJones[13][12] =  43; aaJones[13][13] =   0; aaJones[13][14] =  17; 
aaJones[13][15] =  92; aaJones[13][16] =  12; aaJones[13][17] =  53; aaJones[13][18] = 536; aaJones[13][19] =  62; 
aaJones[14][ 0] = 194; aaJones[14][ 1] =  74; aaJones[14][ 2] =  15; aaJones[14][ 3] =  15; aaJones[14][ 4] =  14; 
aaJones[14][ 5] = 164; aaJones[14][ 6] =  18; aaJones[14][ 7] =  24; aaJones[14][ 8] = 115; aaJones[14][ 9] =  10; 
aaJones[14][10] = 102; aaJones[14][11] =  21; aaJones[14][12] =  16; aaJones[14][13] =  17; aaJones[14][14] =   0; 
aaJones[14][15] = 285; aaJones[14][16] = 118; aaJones[14][17] =   6; aaJones[14][18] =  10; aaJones[14][19] =  23; 
aaJones[15][ 0] = 378; aaJones[15][ 1] = 101; aaJones[15][ 2] = 503; aaJones[15][ 3] =  59; aaJones[15][ 4] = 223; 
aaJones[15][ 5] =  53; aaJones[15][ 6] =  30; aaJones[15][ 7] = 201; aaJones[15][ 8] =  73; aaJones[15][ 9] =  40; 
aaJones[15][10] =  59; aaJones[15][11] =  47; aaJones[15][12] =  29; aaJones[15][13] =  92; aaJones[15][14] = 285; 
aaJones[15][15] =   0; aaJones[15][16] = 477; aaJones[15][17] =  35; aaJones[15][18] =  63; aaJones[15][19] =  38; 
aaJones[16][ 0] = 475; aaJones[16][ 1] =  64; aaJones[16][ 2] = 232; aaJones[16][ 3] =  38; aaJones[16][ 4] =  42; 
aaJones[16][ 5] =  51; aaJones[16][ 6] =  32; aaJones[16][ 7] =  33; aaJones[16][ 8] =  46; aaJones[16][ 9] = 245; 
aaJones[16][10] =  25; aaJones[16][11] = 103; aaJones[16][12] = 226; aaJones[16][13] =  12; aaJones[16][14] = 118; 
aaJones[16][15] = 477; aaJones[16][16] =   0; aaJones[16][17] =  12; aaJones[16][18] =  21; aaJones[16][19] = 112; 
aaJones[17][ 0] =   9; aaJones[17][ 1] = 126; aaJones[17][ 2] =   8; aaJones[17][ 3] =   4; aaJones[17][ 4] = 115; 
aaJones[17][ 5] =  18; aaJones[17][ 6] =  10; aaJones[17][ 7] =  55; aaJones[17][ 8] =   8; aaJones[17][ 9] =   9; 
aaJones[17][10] =  52; aaJones[17][11] =  10; aaJones[17][12] =  24; aaJones[17][13] =  53; aaJones[17][14] =   6; 
aaJones[17][15] =  35; aaJones[17][16] =  12; aaJones[17][17] =   0; aaJones[17][18] =  71; aaJones[17][19] =  25; 
aaJones[18][ 0] =  11; aaJones[18][ 1] =  20; aaJones[18][ 2] =  70; aaJones[18][ 3] =  46; aaJones[18][ 4] = 209; 
aaJones[18][ 5] =  24; aaJones[18][ 6] =   7; aaJones[18][ 7] =   8; aaJones[18][ 8] = 573; aaJones[18][ 9] =  32; 
aaJones[18][10] =  24; aaJones[18][11] =   8; aaJones[18][12] =  18; aaJones[18][13] = 536; aaJones[18][14] =  10; 
aaJones[18][15] =  63; aaJones[18][16] =  21; aaJones[18][17] =  71; aaJones[18][18] =   0; aaJones[18][19] =  16; 
aaJones[19][ 0] = 298; aaJones[19][ 1] =  17; aaJones[19][ 2] =  16; aaJones[19][ 3] =  31; aaJones[19][ 4] =  62; 
aaJones[19][ 5] =  20; aaJones[19][ 6] =  45; aaJones[19][ 7] =  47; aaJones[19][ 8] =  11; aaJones[19][ 9] = 961; 
aaJones[19][10] = 180; aaJones[19][11] =  14; aaJones[19][12] = 323; aaJones[19][13] =  62; aaJones[19][14] =  23; 
aaJones[19][15] =  38; aaJones[19][16] = 112; aaJones[19][17] =  25; aaJones[19][18] =  16; aaJones[19][19] =   0;

out=""
for i in range(20):
    for j in range(0,i):
        out+=str(aaJones[i][j])+" "
    out+="\n"

jonesPi=20*[0]
jonesPi[ 0] = 0.076748;
jonesPi[ 1] = 0.051691;
jonesPi[ 2] = 0.042645;
jonesPi[ 3] = 0.051544;
jonesPi[ 4] = 0.019803;
jonesPi[ 5] = 0.040752;
jonesPi[ 6] = 0.061830;
jonesPi[ 7] = 0.073152;
jonesPi[ 8] = 0.022944;
jonesPi[ 9] = 0.053761;
jonesPi[10] = 0.091904;
jonesPi[11] = 0.058676;
jonesPi[12] = 0.023826;
jonesPi[13] = 0.040126;
jonesPi[14] = 0.050901;
jonesPi[15] = 0.068765;
jonesPi[16] = 0.058565;
jonesPi[17] = 0.014261;
jonesPi[18] = 0.032102;
jonesPi[19] = 0.066005;

for i in range(20):
    if (i/7==i/7.0):out+="\n"
    out+=str(jonesPi[i])+" "

out+="// this is the end of the file."
handle=open("JonesMrBayes.dat","w")
handle.write(out)
handle.close()
    
    
#dayhoff
aaDayhoff=20*[["0"*20]]
aaDayhoff=[i[0].split("0") for i in aaDayhoff]
aaDayhoff[ 0][ 0] =   0; aaDayhoff[ 0][ 1] =  27; aaDayhoff[ 0][ 2] =  98; aaDayhoff[ 0][ 3] = 120; aaDayhoff[ 0][ 4] =  36; 
aaDayhoff[ 0][ 5] =  89; aaDayhoff[ 0][ 6] = 198; aaDayhoff[ 0][ 7] = 240; aaDayhoff[ 0][ 8] =  23; aaDayhoff[ 0][ 9] =  65; 
aaDayhoff[ 0][10] =  41; aaDayhoff[ 0][11] =  26; aaDayhoff[ 0][12] =  72; aaDayhoff[ 0][13] =  18; aaDayhoff[ 0][14] = 250; 
aaDayhoff[ 0][15] = 409; aaDayhoff[ 0][16] = 371; aaDayhoff[ 0][17] =   0; aaDayhoff[ 0][18] =  24; aaDayhoff[ 0][19] = 208; 
aaDayhoff[ 1][ 0] =  27; aaDayhoff[ 1][ 1] =   0; aaDayhoff[ 1][ 2] =  32; aaDayhoff[ 1][ 3] =   0; aaDayhoff[ 1][ 4] =  23; 
aaDayhoff[ 1][ 5] = 246; aaDayhoff[ 1][ 6] =   1; aaDayhoff[ 1][ 7] =   9; aaDayhoff[ 1][ 8] = 240; aaDayhoff[ 1][ 9] =  64; 
aaDayhoff[ 1][10] =  15; aaDayhoff[ 1][11] = 464; aaDayhoff[ 1][12] =  90; aaDayhoff[ 1][13] =  14; aaDayhoff[ 1][14] = 103; 
aaDayhoff[ 1][15] = 154; aaDayhoff[ 1][16] =  26; aaDayhoff[ 1][17] = 201; aaDayhoff[ 1][18] =   8; aaDayhoff[ 1][19] =  24; 
aaDayhoff[ 2][ 0] =  98; aaDayhoff[ 2][ 1] =  32; aaDayhoff[ 2][ 2] =   0; aaDayhoff[ 2][ 3] = 905; aaDayhoff[ 2][ 4] =   0; 
aaDayhoff[ 2][ 5] = 103; aaDayhoff[ 2][ 6] = 148; aaDayhoff[ 2][ 7] = 139; aaDayhoff[ 2][ 8] = 535; aaDayhoff[ 2][ 9] =  77; 
aaDayhoff[ 2][10] =  34; aaDayhoff[ 2][11] = 318; aaDayhoff[ 2][12] =   1; aaDayhoff[ 2][13] =  14; aaDayhoff[ 2][14] =  42; 
aaDayhoff[ 2][15] = 495; aaDayhoff[ 2][16] = 229; aaDayhoff[ 2][17] =  23; aaDayhoff[ 2][18] =  95; aaDayhoff[ 2][19] =  15; 
aaDayhoff[ 3][ 0] = 120; aaDayhoff[ 3][ 1] =   0; aaDayhoff[ 3][ 2] = 905; aaDayhoff[ 3][ 3] =   0; aaDayhoff[ 3][ 4] =   0; 
aaDayhoff[ 3][ 5] = 134; aaDayhoff[ 3][ 6] = 1153; aaDayhoff[ 3][ 7] = 125; aaDayhoff[ 3][ 8] =  86; aaDayhoff[ 3][ 9] =  24; 
aaDayhoff[ 3][10] =   0; aaDayhoff[ 3][11] =  71; aaDayhoff[ 3][12] =   0; aaDayhoff[ 3][13] =   0; aaDayhoff[ 3][14] =  13; 
aaDayhoff[ 3][15] =  95; aaDayhoff[ 3][16] =  66; aaDayhoff[ 3][17] =   0; aaDayhoff[ 3][18] =   0; aaDayhoff[ 3][19] =  18; 
aaDayhoff[ 4][ 0] =  36; aaDayhoff[ 4][ 1] =  23; aaDayhoff[ 4][ 2] =   0; aaDayhoff[ 4][ 3] =   0; aaDayhoff[ 4][ 4] =   0; 
aaDayhoff[ 4][ 5] =   0; aaDayhoff[ 4][ 6] =   0; aaDayhoff[ 4][ 7] =  11; aaDayhoff[ 4][ 8] =  28; aaDayhoff[ 4][ 9] =  44; 
aaDayhoff[ 4][10] =   0; aaDayhoff[ 4][11] =   0; aaDayhoff[ 4][12] =   0; aaDayhoff[ 4][13] =   0; aaDayhoff[ 4][14] =  19; 
aaDayhoff[ 4][15] = 161; aaDayhoff[ 4][16] =  16; aaDayhoff[ 4][17] =   0; aaDayhoff[ 4][18] =  96; aaDayhoff[ 4][19] =  49; 
aaDayhoff[ 5][ 0] =  89; aaDayhoff[ 5][ 1] = 246; aaDayhoff[ 5][ 2] = 103; aaDayhoff[ 5][ 3] = 134; aaDayhoff[ 5][ 4] =   0; 
aaDayhoff[ 5][ 5] =   0; aaDayhoff[ 5][ 6] = 716; aaDayhoff[ 5][ 7] =  28; aaDayhoff[ 5][ 8] = 606; aaDayhoff[ 5][ 9] =  18; 
aaDayhoff[ 5][10] =  73; aaDayhoff[ 5][11] = 153; aaDayhoff[ 5][12] = 114; aaDayhoff[ 5][13] =   0; aaDayhoff[ 5][14] = 153; 
aaDayhoff[ 5][15] =  56; aaDayhoff[ 5][16] =  53; aaDayhoff[ 5][17] =   0; aaDayhoff[ 5][18] =   0; aaDayhoff[ 5][19] =  35; 
aaDayhoff[ 6][ 0] = 198; aaDayhoff[ 6][ 1] =   1; aaDayhoff[ 6][ 2] = 148; aaDayhoff[ 6][ 3] = 1153; aaDayhoff[ 6][ 4] =   0; 
aaDayhoff[ 6][ 5] = 716; aaDayhoff[ 6][ 6] =   0; aaDayhoff[ 6][ 7] =  81; aaDayhoff[ 6][ 8] =  43; aaDayhoff[ 6][ 9] =  61; 
aaDayhoff[ 6][10] =  11; aaDayhoff[ 6][11] =  83; aaDayhoff[ 6][12] =  30; aaDayhoff[ 6][13] =   0; aaDayhoff[ 6][14] =  51; 
aaDayhoff[ 6][15] =  79; aaDayhoff[ 6][16] =  34; aaDayhoff[ 6][17] =   0; aaDayhoff[ 6][18] =  22; aaDayhoff[ 6][19] =  37; 
aaDayhoff[ 7][ 0] = 240; aaDayhoff[ 7][ 1] =   9; aaDayhoff[ 7][ 2] = 139; aaDayhoff[ 7][ 3] = 125; aaDayhoff[ 7][ 4] =  11; 
aaDayhoff[ 7][ 5] =  28; aaDayhoff[ 7][ 6] =  81; aaDayhoff[ 7][ 7] =   0; aaDayhoff[ 7][ 8] =  10; aaDayhoff[ 7][ 9] =   0; 
aaDayhoff[ 7][10] =   7; aaDayhoff[ 7][11] =  27; aaDayhoff[ 7][12] =  17; aaDayhoff[ 7][13] =  15; aaDayhoff[ 7][14] =  34; 
aaDayhoff[ 7][15] = 234; aaDayhoff[ 7][16] =  30; aaDayhoff[ 7][17] =   0; aaDayhoff[ 7][18] =   0; aaDayhoff[ 7][19] =  54; 
aaDayhoff[ 8][ 0] =  23; aaDayhoff[ 8][ 1] = 240; aaDayhoff[ 8][ 2] = 535; aaDayhoff[ 8][ 3] =  86; aaDayhoff[ 8][ 4] =  28; 
aaDayhoff[ 8][ 5] = 606; aaDayhoff[ 8][ 6] =  43; aaDayhoff[ 8][ 7] =  10; aaDayhoff[ 8][ 8] =   0; aaDayhoff[ 8][ 9] =   7; 
aaDayhoff[ 8][10] =  44; aaDayhoff[ 8][11] =  26; aaDayhoff[ 8][12] =   0; aaDayhoff[ 8][13] =  48; aaDayhoff[ 8][14] =  94; 
aaDayhoff[ 8][15] =  35; aaDayhoff[ 8][16] =  22; aaDayhoff[ 8][17] =  27; aaDayhoff[ 8][18] = 127; aaDayhoff[ 8][19] =  44; 
aaDayhoff[ 9][ 0] =  65; aaDayhoff[ 9][ 1] =  64; aaDayhoff[ 9][ 2] =  77; aaDayhoff[ 9][ 3] =  24; aaDayhoff[ 9][ 4] =  44; 
aaDayhoff[ 9][ 5] =  18; aaDayhoff[ 9][ 6] =  61; aaDayhoff[ 9][ 7] =   0; aaDayhoff[ 9][ 8] =   7; aaDayhoff[ 9][ 9] =   0; 
aaDayhoff[ 9][10] = 257; aaDayhoff[ 9][11] =  46; aaDayhoff[ 9][12] = 336; aaDayhoff[ 9][13] = 196; aaDayhoff[ 9][14] =  12; 
aaDayhoff[ 9][15] =  24; aaDayhoff[ 9][16] = 192; aaDayhoff[ 9][17] =   0; aaDayhoff[ 9][18] =  37; aaDayhoff[ 9][19] = 889; 
aaDayhoff[10][ 0] =  41; aaDayhoff[10][ 1] =  15; aaDayhoff[10][ 2] =  34; aaDayhoff[10][ 3] =   0; aaDayhoff[10][ 4] =   0; 
aaDayhoff[10][ 5] =  73; aaDayhoff[10][ 6] =  11; aaDayhoff[10][ 7] =   7; aaDayhoff[10][ 8] =  44; aaDayhoff[10][ 9] = 257; 
aaDayhoff[10][10] =   0; aaDayhoff[10][11] =  18; aaDayhoff[10][12] = 527; aaDayhoff[10][13] = 157; aaDayhoff[10][14] =  32; 
aaDayhoff[10][15] =  17; aaDayhoff[10][16] =  33; aaDayhoff[10][17] =  46; aaDayhoff[10][18] =  28; aaDayhoff[10][19] = 175; 
aaDayhoff[11][ 0] =  26; aaDayhoff[11][ 1] = 464; aaDayhoff[11][ 2] = 318; aaDayhoff[11][ 3] =  71; aaDayhoff[11][ 4] =   0; 
aaDayhoff[11][ 5] = 153; aaDayhoff[11][ 6] =  83; aaDayhoff[11][ 7] =  27; aaDayhoff[11][ 8] =  26; aaDayhoff[11][ 9] =  46; 
aaDayhoff[11][10] =  18; aaDayhoff[11][11] =   0; aaDayhoff[11][12] = 243; aaDayhoff[11][13] =   0; aaDayhoff[11][14] =  33; 
aaDayhoff[11][15] =  96; aaDayhoff[11][16] = 136; aaDayhoff[11][17] =   0; aaDayhoff[11][18] =  13; aaDayhoff[11][19] =  10; 
aaDayhoff[12][ 0] =  72; aaDayhoff[12][ 1] =  90; aaDayhoff[12][ 2] =   1; aaDayhoff[12][ 3] =   0; aaDayhoff[12][ 4] =   0; 
aaDayhoff[12][ 5] = 114; aaDayhoff[12][ 6] =  30; aaDayhoff[12][ 7] =  17; aaDayhoff[12][ 8] =   0; aaDayhoff[12][ 9] = 336; 
aaDayhoff[12][10] = 527; aaDayhoff[12][11] = 243; aaDayhoff[12][12] =   0; aaDayhoff[12][13] =  92; aaDayhoff[12][14] =  17; 
aaDayhoff[12][15] =  62; aaDayhoff[12][16] = 104; aaDayhoff[12][17] =   0; aaDayhoff[12][18] =   0; aaDayhoff[12][19] = 258; 
aaDayhoff[13][ 0] =  18; aaDayhoff[13][ 1] =  14; aaDayhoff[13][ 2] =  14; aaDayhoff[13][ 3] =   0; aaDayhoff[13][ 4] =   0; 
aaDayhoff[13][ 5] =   0; aaDayhoff[13][ 6] =   0; aaDayhoff[13][ 7] =  15; aaDayhoff[13][ 8] =  48; aaDayhoff[13][ 9] = 196; 
aaDayhoff[13][10] = 157; aaDayhoff[13][11] =   0; aaDayhoff[13][12] =  92; aaDayhoff[13][13] =   0; aaDayhoff[13][14] =  11; 
aaDayhoff[13][15] =  46; aaDayhoff[13][16] =  13; aaDayhoff[13][17] =  76; aaDayhoff[13][18] = 698; aaDayhoff[13][19] =  12; 
aaDayhoff[14][ 0] = 250; aaDayhoff[14][ 1] = 103; aaDayhoff[14][ 2] =  42; aaDayhoff[14][ 3] =  13; aaDayhoff[14][ 4] =  19; 
aaDayhoff[14][ 5] = 153; aaDayhoff[14][ 6] =  51; aaDayhoff[14][ 7] =  34; aaDayhoff[14][ 8] =  94; aaDayhoff[14][ 9] =  12; 
aaDayhoff[14][10] =  32; aaDayhoff[14][11] =  33; aaDayhoff[14][12] =  17; aaDayhoff[14][13] =  11; aaDayhoff[14][14] =   0; 
aaDayhoff[14][15] = 245; aaDayhoff[14][16] =  78; aaDayhoff[14][17] =   0; aaDayhoff[14][18] =   0; aaDayhoff[14][19] =  48; 
aaDayhoff[15][ 0] = 409; aaDayhoff[15][ 1] = 154; aaDayhoff[15][ 2] = 495; aaDayhoff[15][ 3] =  95; aaDayhoff[15][ 4] = 161; 
aaDayhoff[15][ 5] =  56; aaDayhoff[15][ 6] =  79; aaDayhoff[15][ 7] = 234; aaDayhoff[15][ 8] =  35; aaDayhoff[15][ 9] =  24; 
aaDayhoff[15][10] =  17; aaDayhoff[15][11] =  96; aaDayhoff[15][12] =  62; aaDayhoff[15][13] =  46; aaDayhoff[15][14] = 245; 
aaDayhoff[15][15] =   0; aaDayhoff[15][16] = 550; aaDayhoff[15][17] =  75; aaDayhoff[15][18] =  34; aaDayhoff[15][19] =  30; 
aaDayhoff[16][ 0] = 371; aaDayhoff[16][ 1] =  26; aaDayhoff[16][ 2] = 229; aaDayhoff[16][ 3] =  66; aaDayhoff[16][ 4] =  16; 
aaDayhoff[16][ 5] =  53; aaDayhoff[16][ 6] =  34; aaDayhoff[16][ 7] =  30; aaDayhoff[16][ 8] =  22; aaDayhoff[16][ 9] = 192; 
aaDayhoff[16][10] =  33; aaDayhoff[16][11] = 136; aaDayhoff[16][12] = 104; aaDayhoff[16][13] =  13; aaDayhoff[16][14] =  78; 
aaDayhoff[16][15] = 550; aaDayhoff[16][16] =   0; aaDayhoff[16][17] =   0; aaDayhoff[16][18] =  42; aaDayhoff[16][19] = 157; 
aaDayhoff[17][ 0] =   0; aaDayhoff[17][ 1] = 201; aaDayhoff[17][ 2] =  23; aaDayhoff[17][ 3] =   0; aaDayhoff[17][ 4] =   0; 
aaDayhoff[17][ 5] =   0; aaDayhoff[17][ 6] =   0; aaDayhoff[17][ 7] =   0; aaDayhoff[17][ 8] =  27; aaDayhoff[17][ 9] =   0; 
aaDayhoff[17][10] =  46; aaDayhoff[17][11] =   0; aaDayhoff[17][12] =   0; aaDayhoff[17][13] =  76; aaDayhoff[17][14] =   0; 
aaDayhoff[17][15] =  75; aaDayhoff[17][16] =   0; aaDayhoff[17][17] =   0; aaDayhoff[17][18] =  61; aaDayhoff[17][19] =   0; 
aaDayhoff[18][ 0] =  24; aaDayhoff[18][ 1] =   8; aaDayhoff[18][ 2] =  95; aaDayhoff[18][ 3] =   0; aaDayhoff[18][ 4] =  96; 
aaDayhoff[18][ 5] =   0; aaDayhoff[18][ 6] =  22; aaDayhoff[18][ 7] =   0; aaDayhoff[18][ 8] = 127; aaDayhoff[18][ 9] =  37; 
aaDayhoff[18][10] =  28; aaDayhoff[18][11] =  13; aaDayhoff[18][12] =   0; aaDayhoff[18][13] = 698; aaDayhoff[18][14] =   0; 
aaDayhoff[18][15] =  34; aaDayhoff[18][16] =  42; aaDayhoff[18][17] =  61; aaDayhoff[18][18] =   0; aaDayhoff[18][19] =  28; 
aaDayhoff[19][ 0] = 208; aaDayhoff[19][ 1] =  24; aaDayhoff[19][ 2] =  15; aaDayhoff[19][ 3] =  18; aaDayhoff[19][ 4] =  49; 
aaDayhoff[19][ 5] =  35; aaDayhoff[19][ 6] =  37; aaDayhoff[19][ 7] =  54; aaDayhoff[19][ 8] =  44; aaDayhoff[19][ 9] = 889; 
aaDayhoff[19][10] = 175; aaDayhoff[19][11] =  10; aaDayhoff[19][12] = 258; aaDayhoff[19][13] =  12; aaDayhoff[19][14] =  48; 
aaDayhoff[19][15] =  30; aaDayhoff[19][16] = 157; aaDayhoff[19][17] =   0; aaDayhoff[19][18] =  28; aaDayhoff[19][19] =   0;

dayhoffPi=20*[0]
dayhoffPi[ 0] = 0.087127;
dayhoffPi[ 1] = 0.040904;
dayhoffPi[ 2] = 0.040432;
dayhoffPi[ 3] = 0.046872;
dayhoffPi[ 4] = 0.033474;
dayhoffPi[ 5] = 0.038255;
dayhoffPi[ 6] = 0.049530;
dayhoffPi[ 7] = 0.088612;
dayhoffPi[ 8] = 0.033618;
dayhoffPi[ 9] = 0.036886;
dayhoffPi[10] = 0.085357;
dayhoffPi[11] = 0.080482;
dayhoffPi[12] = 0.014753;
dayhoffPi[13] = 0.039772;
dayhoffPi[14] = 0.050680;
dayhoffPi[15] = 0.069577;
dayhoffPi[16] = 0.058542;
dayhoffPi[17] = 0.010494;
dayhoffPi[18] = 0.029916;
dayhoffPi[19] = 0.064718;

out=""
for i in range(20):
    for j in range(0,i):
        out+=str(aaDayhoff[i][j])+" "
    out+="\n"

for i in range(20):
    if (i/7==i/7.0):out+="\n"
    out+=str(dayhoffPi[i])+" "

out+="// this is the end of the file."
handle=open("DayhoffMrBayes.dat","w")
handle.write(out)
handle.close()

#mtrev24
aaMtrev24=20*[["0"*20]]
aaMtrev24=[i[0].split("0") for i in aaMtrev24]
aaMtrev24[ 0][ 0] =   0.00; aaMtrev24[ 0][ 1] =  23.18; aaMtrev24[ 0][ 2] =  26.95; aaMtrev24[ 0][ 3] =  17.67; aaMtrev24[ 0][ 4] =  59.93;
aaMtrev24[ 0][ 5] =   1.90; aaMtrev24[ 0][ 6] =   9.77; aaMtrev24[ 0][ 7] = 120.71; aaMtrev24[ 0][ 8] =  13.90; aaMtrev24[ 0][ 9] =  96.49;
aaMtrev24[ 0][10] =  25.46; aaMtrev24[ 0][11] =   8.36; aaMtrev24[ 0][12] = 141.88; aaMtrev24[ 0][13] =   6.37; aaMtrev24[ 0][14] =  54.31;
aaMtrev24[ 0][15] = 387.86; aaMtrev24[ 0][16] = 480.72; aaMtrev24[ 0][17] =   1.90; aaMtrev24[ 0][18] =   6.48; aaMtrev24[ 0][19] = 195.06;
aaMtrev24[ 1][ 0] =  23.18; aaMtrev24[ 1][ 1] =   0.00; aaMtrev24[ 1][ 2] =  13.24; aaMtrev24[ 1][ 3] =   1.90; aaMtrev24[ 1][ 4] = 103.33;
aaMtrev24[ 1][ 5] = 220.99; aaMtrev24[ 1][ 6] =   1.90; aaMtrev24[ 1][ 7] =  23.03; aaMtrev24[ 1][ 8] = 165.23; aaMtrev24[ 1][ 9] =   1.90;
aaMtrev24[ 1][10] =  15.58; aaMtrev24[ 1][11] = 141.40; aaMtrev24[ 1][12] =   1.90; aaMtrev24[ 1][13] =   4.69; aaMtrev24[ 1][14] =  23.64;
aaMtrev24[ 1][15] =   6.04; aaMtrev24[ 1][16] =   2.08; aaMtrev24[ 1][17] =  21.95; aaMtrev24[ 1][18] =   1.90; aaMtrev24[ 1][19] =   7.64;
aaMtrev24[ 2][ 0] =  26.95; aaMtrev24[ 2][ 1] =  13.24; aaMtrev24[ 2][ 2] =   0.00; aaMtrev24[ 2][ 3] = 794.38; aaMtrev24[ 2][ 4] =  58.94;
aaMtrev24[ 2][ 5] = 173.56; aaMtrev24[ 2][ 6] =  63.05; aaMtrev24[ 2][ 7] =  53.30; aaMtrev24[ 2][ 8] = 496.13; aaMtrev24[ 2][ 9] =  27.10;
aaMtrev24[ 2][10] =  15.16; aaMtrev24[ 2][11] = 608.70; aaMtrev24[ 2][12] =  65.41; aaMtrev24[ 2][13] =  15.20; aaMtrev24[ 2][14] =  73.31;
aaMtrev24[ 2][15] = 494.39; aaMtrev24[ 2][16] = 238.46; aaMtrev24[ 2][17] =  10.68; aaMtrev24[ 2][18] = 191.36; aaMtrev24[ 2][19] =   1.90;
aaMtrev24[ 3][ 0] =  17.67; aaMtrev24[ 3][ 1] =   1.90; aaMtrev24[ 3][ 2] = 794.38; aaMtrev24[ 3][ 3] =   0.00; aaMtrev24[ 3][ 4] =   1.90;
aaMtrev24[ 3][ 5] =  55.28; aaMtrev24[ 3][ 6] = 583.55; aaMtrev24[ 3][ 7] =  56.77; aaMtrev24[ 3][ 8] = 113.99; aaMtrev24[ 3][ 9] =   4.34;
aaMtrev24[ 3][10] =   1.90; aaMtrev24[ 3][11] =   2.31; aaMtrev24[ 3][12] =   1.90; aaMtrev24[ 3][13] =   4.98; aaMtrev24[ 3][14] =  13.43;
aaMtrev24[ 3][15] =  69.02; aaMtrev24[ 3][16] =  28.01; aaMtrev24[ 3][17] =  19.86; aaMtrev24[ 3][18] =  21.21; aaMtrev24[ 3][19] =   1.90;
aaMtrev24[ 4][ 0] =  59.93; aaMtrev24[ 4][ 1] = 103.33; aaMtrev24[ 4][ 2] =  58.94; aaMtrev24[ 4][ 3] =   1.90; aaMtrev24[ 4][ 4] =   0.00;
aaMtrev24[ 4][ 5] =  75.24; aaMtrev24[ 4][ 6] =   1.90; aaMtrev24[ 4][ 7] =  30.71; aaMtrev24[ 4][ 8] = 141.49; aaMtrev24[ 4][ 9] =  62.73;
aaMtrev24[ 4][10] =  25.65; aaMtrev24[ 4][11] =   1.90; aaMtrev24[ 4][12] =   6.18; aaMtrev24[ 4][13] =  70.80; aaMtrev24[ 4][14] =  31.26;
aaMtrev24[ 4][15] = 277.05; aaMtrev24[ 4][16] = 179.97; aaMtrev24[ 4][17] =  33.60; aaMtrev24[ 4][18] = 254.77; aaMtrev24[ 4][19] =   1.90;
aaMtrev24[ 5][ 0] =   1.90; aaMtrev24[ 5][ 1] = 220.99; aaMtrev24[ 5][ 2] = 173.56; aaMtrev24[ 5][ 3] =  55.28; aaMtrev24[ 5][ 4] =  75.24;
aaMtrev24[ 5][ 5] =   0.00; aaMtrev24[ 5][ 6] = 313.56; aaMtrev24[ 5][ 7] =   6.75; aaMtrev24[ 5][ 8] = 582.40; aaMtrev24[ 5][ 9] =   8.34;
aaMtrev24[ 5][10] =  39.70; aaMtrev24[ 5][11] = 465.58; aaMtrev24[ 5][12] =  47.37; aaMtrev24[ 5][13] =  19.11; aaMtrev24[ 5][14] = 137.29;
aaMtrev24[ 5][15] =  54.11; aaMtrev24[ 5][16] =  94.93; aaMtrev24[ 5][17] =   1.90; aaMtrev24[ 5][18] =  38.82; aaMtrev24[ 5][19] =  19.00;
aaMtrev24[ 6][ 0] =   9.77; aaMtrev24[ 6][ 1] =   1.90; aaMtrev24[ 6][ 2] =  63.05; aaMtrev24[ 6][ 3] = 583.55; aaMtrev24[ 6][ 4] =   1.90;
aaMtrev24[ 6][ 5] = 313.56; aaMtrev24[ 6][ 6] =   0.00; aaMtrev24[ 6][ 7] =  28.28; aaMtrev24[ 6][ 8] =  49.12; aaMtrev24[ 6][ 9] =   3.31;
aaMtrev24[ 6][10] =   1.90; aaMtrev24[ 6][11] = 313.86; aaMtrev24[ 6][12] =   1.90; aaMtrev24[ 6][13] =   2.67; aaMtrev24[ 6][14] =  12.83;
aaMtrev24[ 6][15] =  54.71; aaMtrev24[ 6][16] =  14.82; aaMtrev24[ 6][17] =   1.90; aaMtrev24[ 6][18] =  13.12; aaMtrev24[ 6][19] =  21.14;
aaMtrev24[ 7][ 0] = 120.71; aaMtrev24[ 7][ 1] =  23.03; aaMtrev24[ 7][ 2] =  53.30; aaMtrev24[ 7][ 3] =  56.77; aaMtrev24[ 7][ 4] =  30.71;
aaMtrev24[ 7][ 5] =   6.75; aaMtrev24[ 7][ 6] =  28.28; aaMtrev24[ 7][ 7] =   0.00; aaMtrev24[ 7][ 8] =   1.90; aaMtrev24[ 7][ 9] =   5.98;
aaMtrev24[ 7][10] =   2.41; aaMtrev24[ 7][11] =  22.73; aaMtrev24[ 7][12] =   1.90; aaMtrev24[ 7][13] =   1.90; aaMtrev24[ 7][14] =   1.90;
aaMtrev24[ 7][15] = 125.93; aaMtrev24[ 7][16] =  11.17; aaMtrev24[ 7][17] =  10.92; aaMtrev24[ 7][18] =   3.21; aaMtrev24[ 7][19] =   2.53;
aaMtrev24[ 8][ 0] =  13.90; aaMtrev24[ 8][ 1] = 165.23; aaMtrev24[ 8][ 2] = 496.13; aaMtrev24[ 8][ 3] = 113.99; aaMtrev24[ 8][ 4] = 141.49;
aaMtrev24[ 8][ 5] = 582.40; aaMtrev24[ 8][ 6] =  49.12; aaMtrev24[ 8][ 7] =   1.90; aaMtrev24[ 8][ 8] =   0.00; aaMtrev24[ 8][ 9] =  12.26;
aaMtrev24[ 8][10] =  11.49; aaMtrev24[ 8][11] = 127.67; aaMtrev24[ 8][12] =  11.97; aaMtrev24[ 8][13] =  48.16; aaMtrev24[ 8][14] =  60.97;
aaMtrev24[ 8][15] =  77.46; aaMtrev24[ 8][16] =  44.78; aaMtrev24[ 8][17] =   7.08; aaMtrev24[ 8][18] = 670.14; aaMtrev24[ 8][19] =   1.90;
aaMtrev24[ 9][ 0] =  96.49; aaMtrev24[ 9][ 1] =   1.90; aaMtrev24[ 9][ 2] =  27.10; aaMtrev24[ 9][ 3] =   4.34; aaMtrev24[ 9][ 4] =  62.73;
aaMtrev24[ 9][ 5] =   8.34; aaMtrev24[ 9][ 6] =   3.31; aaMtrev24[ 9][ 7] =   5.98; aaMtrev24[ 9][ 8] =  12.26; aaMtrev24[ 9][ 9] =   0.00;
aaMtrev24[ 9][10] = 329.09; aaMtrev24[ 9][11] =  19.57; aaMtrev24[ 9][12] = 517.98; aaMtrev24[ 9][13] =  84.67; aaMtrev24[ 9][14] =  20.63;
aaMtrev24[ 9][15] =  47.70; aaMtrev24[ 9][16] = 368.43; aaMtrev24[ 9][17] =   1.90; aaMtrev24[ 9][18] =  25.01; aaMtrev24[ 9][19] =1222.94;
aaMtrev24[10][ 0] =  25.46; aaMtrev24[10][ 1] =  15.58; aaMtrev24[10][ 2] =  15.16; aaMtrev24[10][ 3] =   1.90; aaMtrev24[10][ 4] =  25.65;
aaMtrev24[10][ 5] =  39.70; aaMtrev24[10][ 6] =   1.90; aaMtrev24[10][ 7] =   2.41; aaMtrev24[10][ 8] =  11.49; aaMtrev24[10][ 9] = 329.09;
aaMtrev24[10][10] =   0.00; aaMtrev24[10][11] =  14.88; aaMtrev24[10][12] = 537.53; aaMtrev24[10][13] = 216.06; aaMtrev24[10][14] =  40.10;
aaMtrev24[10][15] =  73.61; aaMtrev24[10][16] = 126.40; aaMtrev24[10][17] =  32.44; aaMtrev24[10][18] =  44.15; aaMtrev24[10][19] =  91.67;
aaMtrev24[11][ 0] =   8.36; aaMtrev24[11][ 1] = 141.40; aaMtrev24[11][ 2] = 608.70; aaMtrev24[11][ 3] =   2.31; aaMtrev24[11][ 4] =   1.90;
aaMtrev24[11][ 5] = 465.58; aaMtrev24[11][ 6] = 313.86; aaMtrev24[11][ 7] =  22.73; aaMtrev24[11][ 8] = 127.67; aaMtrev24[11][ 9] =  19.57;
aaMtrev24[11][10] =  14.88; aaMtrev24[11][11] =   0.00; aaMtrev24[11][12] =  91.37; aaMtrev24[11][13] =   6.44; aaMtrev24[11][14] =  50.10;
aaMtrev24[11][15] = 105.79; aaMtrev24[11][16] = 136.33; aaMtrev24[11][17] =  24.00; aaMtrev24[11][18] =  51.17; aaMtrev24[11][19] =   1.90;
aaMtrev24[12][ 0] = 141.88; aaMtrev24[12][ 1] =   1.90; aaMtrev24[12][ 2] =  65.41; aaMtrev24[12][ 3] =   1.90; aaMtrev24[12][ 4] =   6.18;
aaMtrev24[12][ 5] =  47.37; aaMtrev24[12][ 6] =   1.90; aaMtrev24[12][ 7] =   1.90; aaMtrev24[12][ 8] =  11.97; aaMtrev24[12][ 9] = 517.98;
aaMtrev24[12][10] = 537.53; aaMtrev24[12][11] =  91.37; aaMtrev24[12][12] =   0.00; aaMtrev24[12][13] =  90.82; aaMtrev24[12][14] =  18.84;
aaMtrev24[12][15] = 111.16; aaMtrev24[12][16] = 528.17; aaMtrev24[12][17] =  21.71; aaMtrev24[12][18] =  39.96; aaMtrev24[12][19] = 387.54;
aaMtrev24[13][ 0] =   6.37; aaMtrev24[13][ 1] =   4.69; aaMtrev24[13][ 2] =  15.20; aaMtrev24[13][ 3] =   4.98; aaMtrev24[13][ 4] =  70.80;
aaMtrev24[13][ 5] =  19.11; aaMtrev24[13][ 6] =   2.67; aaMtrev24[13][ 7] =   1.90; aaMtrev24[13][ 8] =  48.16; aaMtrev24[13][ 9] =  84.67;
aaMtrev24[13][10] = 216.06; aaMtrev24[13][11] =   6.44; aaMtrev24[13][12] =  90.82; aaMtrev24[13][13] =   0.00; aaMtrev24[13][14] =  17.31;
aaMtrev24[13][15] =  64.29; aaMtrev24[13][16] =  33.85; aaMtrev24[13][17] =   7.84; aaMtrev24[13][18] = 465.58; aaMtrev24[13][19] =   6.35;
aaMtrev24[14][ 0] =  54.31; aaMtrev24[14][ 1] =  23.64; aaMtrev24[14][ 2] =  73.31; aaMtrev24[14][ 3] =  13.43; aaMtrev24[14][ 4] =  31.26;
aaMtrev24[14][ 5] = 137.29; aaMtrev24[14][ 6] =  12.83; aaMtrev24[14][ 7] =   1.90; aaMtrev24[14][ 8] =  60.97; aaMtrev24[14][ 9] =  20.63;
aaMtrev24[14][10] =  40.10; aaMtrev24[14][11] =  50.10; aaMtrev24[14][12] =  18.84; aaMtrev24[14][13] =  17.31; aaMtrev24[14][14] =   0.00;
aaMtrev24[14][15] = 169.90; aaMtrev24[14][16] = 128.22; aaMtrev24[14][17] =   4.21; aaMtrev24[14][18] =  16.21; aaMtrev24[14][19] =   8.23;
aaMtrev24[15][ 0] = 387.86; aaMtrev24[15][ 1] =   6.04; aaMtrev24[15][ 2] = 494.39; aaMtrev24[15][ 3] =  69.02; aaMtrev24[15][ 4] = 277.05;
aaMtrev24[15][ 5] =  54.11; aaMtrev24[15][ 6] =  54.71; aaMtrev24[15][ 7] = 125.93; aaMtrev24[15][ 8] =  77.46; aaMtrev24[15][ 9] =  47.70;
aaMtrev24[15][10] =  73.61; aaMtrev24[15][11] = 105.79; aaMtrev24[15][12] = 111.16; aaMtrev24[15][13] =  64.29; aaMtrev24[15][14] = 169.90;
aaMtrev24[15][15] =   0.00; aaMtrev24[15][16] = 597.21; aaMtrev24[15][17] =  38.58; aaMtrev24[15][18] =  64.92; aaMtrev24[15][19] =   1.90;
aaMtrev24[16][ 0] = 480.72; aaMtrev24[16][ 1] =   2.08; aaMtrev24[16][ 2] = 238.46; aaMtrev24[16][ 3] =  28.01; aaMtrev24[16][ 4] = 179.97;
aaMtrev24[16][ 5] =  94.93; aaMtrev24[16][ 6] =  14.82; aaMtrev24[16][ 7] =  11.17; aaMtrev24[16][ 8] =  44.78; aaMtrev24[16][ 9] = 368.43;
aaMtrev24[16][10] = 126.40; aaMtrev24[16][11] = 136.33; aaMtrev24[16][12] = 528.17; aaMtrev24[16][13] =  33.85; aaMtrev24[16][14] = 128.22;
aaMtrev24[16][15] = 597.21; aaMtrev24[16][16] =   0.00; aaMtrev24[16][17] =   9.99; aaMtrev24[16][18] =  38.73; aaMtrev24[16][19] = 204.54;
aaMtrev24[17][ 0] =   1.90; aaMtrev24[17][ 1] =  21.95; aaMtrev24[17][ 2] =  10.68; aaMtrev24[17][ 3] =  19.86; aaMtrev24[17][ 4] =  33.60;
aaMtrev24[17][ 5] =   1.90; aaMtrev24[17][ 6] =   1.90; aaMtrev24[17][ 7] =  10.92; aaMtrev24[17][ 8] =   7.08; aaMtrev24[17][ 9] =   1.90;
aaMtrev24[17][10] =  32.44; aaMtrev24[17][11] =  24.00; aaMtrev24[17][12] =  21.71; aaMtrev24[17][13] =   7.84; aaMtrev24[17][14] =   4.21;
aaMtrev24[17][15] =  38.58; aaMtrev24[17][16] =   9.99; aaMtrev24[17][17] =   0.00; aaMtrev24[17][18] =  26.25; aaMtrev24[17][19] =   5.37;
aaMtrev24[18][ 0] =   6.48; aaMtrev24[18][ 1] =   1.90; aaMtrev24[18][ 2] = 191.36; aaMtrev24[18][ 3] =  21.21; aaMtrev24[18][ 4] = 254.77;
aaMtrev24[18][ 5] =  38.82; aaMtrev24[18][ 6] =  13.12; aaMtrev24[18][ 7] =   3.21; aaMtrev24[18][ 8] = 670.14; aaMtrev24[18][ 9] =  25.01;
aaMtrev24[18][10] =  44.15; aaMtrev24[18][11] =  51.17; aaMtrev24[18][12] =  39.96; aaMtrev24[18][13] = 465.58; aaMtrev24[18][14] =  16.21;
aaMtrev24[18][15] =  64.92; aaMtrev24[18][16] =  38.73; aaMtrev24[18][17] =  26.25; aaMtrev24[18][18] =   0.00; aaMtrev24[18][19] =   1.90;
aaMtrev24[19][ 0] = 195.06; aaMtrev24[19][ 1] =   7.64; aaMtrev24[19][ 2] =   1.90; aaMtrev24[19][ 3] =   1.90; aaMtrev24[19][ 4] =   1.90;
aaMtrev24[19][ 5] =  19.00; aaMtrev24[19][ 6] =  21.14; aaMtrev24[19][ 7] =   2.53; aaMtrev24[19][ 8] =   1.90; aaMtrev24[19][ 9] =1222.94;
aaMtrev24[19][10] =  91.67; aaMtrev24[19][11] =   1.90; aaMtrev24[19][12] = 387.54; aaMtrev24[19][13] =   6.35; aaMtrev24[19][14] =   8.23;
aaMtrev24[19][15] =   1.90; aaMtrev24[19][16] = 204.54; aaMtrev24[19][17] =   5.37; aaMtrev24[19][18] =   1.90; aaMtrev24[19][19] =   0.00;

mtrev24Pi=20*[0]
mtrev24Pi[ 0] = 0.072;
mtrev24Pi[ 1] = 0.019;
mtrev24Pi[ 2] = 0.039;
mtrev24Pi[ 3] = 0.019;
mtrev24Pi[ 4] = 0.006;
mtrev24Pi[ 5] = 0.025;
mtrev24Pi[ 6] = 0.024;
mtrev24Pi[ 7] = 0.056;
mtrev24Pi[ 8] = 0.028;
mtrev24Pi[ 9] = 0.088;
mtrev24Pi[10] = 0.168;
mtrev24Pi[11] = 0.023;
mtrev24Pi[12] = 0.054;
mtrev24Pi[13] = 0.061;
mtrev24Pi[14] = 0.054;
mtrev24Pi[15] = 0.072;
mtrev24Pi[16] = 0.086;
mtrev24Pi[17] = 0.029;
mtrev24Pi[18] = 0.033;
mtrev24Pi[19] = 0.043;

out=""
for i in range(20):
    for j in range(0,i):
        out+=str(aaMtrev24[i][j])+" "
    out+="\n"

for i in range(20):
    if (i/7==i/7.0):out+="\n"
    out+=str(mtrev24Pi[i])+" "

out+="// this is the end of the file."
handle=open("mtrev24MrBayes.dat","w")
handle.write(out)
handle.close()

#mtmam
aaMtmam=20*[["0"*20]]
aaMtmam=[i[0].split("0") for i in aaMtmam]
aaMtmam[ 0][ 0] =   0; aaMtmam[ 0][ 1] =  32; aaMtmam[ 0][ 2] =   2; aaMtmam[ 0][ 3] =  11; aaMtmam[ 0][ 4] =   0;
aaMtmam[ 0][ 5] =   0; aaMtmam[ 0][ 6] =   0; aaMtmam[ 0][ 7] =  78; aaMtmam[ 0][ 8] =   8; aaMtmam[ 0][ 9] =  75;
aaMtmam[ 0][10] =  21; aaMtmam[ 0][11] =   0; aaMtmam[ 0][12] =  76; aaMtmam[ 0][13] =   0; aaMtmam[ 0][14] =  53;
aaMtmam[ 0][15] = 342; aaMtmam[ 0][16] = 681; aaMtmam[ 0][17] =   5; aaMtmam[ 0][18] =   0; aaMtmam[ 0][19] = 398;
aaMtmam[ 1][ 0] =  32; aaMtmam[ 1][ 1] =   0; aaMtmam[ 1][ 2] =   4; aaMtmam[ 1][ 3] =   0; aaMtmam[ 1][ 4] = 186;
aaMtmam[ 1][ 5] = 246; aaMtmam[ 1][ 6] =   0; aaMtmam[ 1][ 7] =  18; aaMtmam[ 1][ 8] = 232; aaMtmam[ 1][ 9] =   0;
aaMtmam[ 1][10] =   6; aaMtmam[ 1][11] =  50; aaMtmam[ 1][12] =   0; aaMtmam[ 1][13] =   0; aaMtmam[ 1][14] =   9;
aaMtmam[ 1][15] =   3; aaMtmam[ 1][16] =   0; aaMtmam[ 1][17] =  16; aaMtmam[ 1][18] =   0; aaMtmam[ 1][19] =   0;
aaMtmam[ 2][ 0] =   2; aaMtmam[ 2][ 1] =   4; aaMtmam[ 2][ 2] =   0; aaMtmam[ 2][ 3] = 864; aaMtmam[ 2][ 4] =   0;
aaMtmam[ 2][ 5] =   8; aaMtmam[ 2][ 6] =   0; aaMtmam[ 2][ 7] =  47; aaMtmam[ 2][ 8] = 458; aaMtmam[ 2][ 9] =  19;
aaMtmam[ 2][10] =   0; aaMtmam[ 2][11] = 408; aaMtmam[ 2][12] =  21; aaMtmam[ 2][13] =   6; aaMtmam[ 2][14] =  33;
aaMtmam[ 2][15] = 446; aaMtmam[ 2][16] = 110; aaMtmam[ 2][17] =   6; aaMtmam[ 2][18] = 156; aaMtmam[ 2][19] =   0;
aaMtmam[ 3][ 0] =  11; aaMtmam[ 3][ 1] =   0; aaMtmam[ 3][ 2] = 864; aaMtmam[ 3][ 3] =   0; aaMtmam[ 3][ 4] =   0;
aaMtmam[ 3][ 5] =  49; aaMtmam[ 3][ 6] = 569; aaMtmam[ 3][ 7] =  79; aaMtmam[ 3][ 8] =  11; aaMtmam[ 3][ 9] =   0;
aaMtmam[ 3][10] =   0; aaMtmam[ 3][11] =   0; aaMtmam[ 3][12] =   0; aaMtmam[ 3][13] =   5; aaMtmam[ 3][14] =   2;
aaMtmam[ 3][15] =  16; aaMtmam[ 3][16] =   0; aaMtmam[ 3][17] =   0; aaMtmam[ 3][18] =   0; aaMtmam[ 3][19] =  10;
aaMtmam[ 4][ 0] =   0; aaMtmam[ 4][ 1] = 186; aaMtmam[ 4][ 2] =   0; aaMtmam[ 4][ 3] =   0; aaMtmam[ 4][ 4] =   0;
aaMtmam[ 4][ 5] =   0; aaMtmam[ 4][ 6] =   0; aaMtmam[ 4][ 7] =   0; aaMtmam[ 4][ 8] = 305; aaMtmam[ 4][ 9] =  41;
aaMtmam[ 4][10] =  27; aaMtmam[ 4][11] =   0; aaMtmam[ 4][12] =   0; aaMtmam[ 4][13] =   7; aaMtmam[ 4][14] =   0;
aaMtmam[ 4][15] = 347; aaMtmam[ 4][16] = 114; aaMtmam[ 4][17] =  65; aaMtmam[ 4][18] = 530; aaMtmam[ 4][19] =   0;
aaMtmam[ 5][ 0] =   0; aaMtmam[ 5][ 1] = 246; aaMtmam[ 5][ 2] =   8; aaMtmam[ 5][ 3] =  49; aaMtmam[ 5][ 4] =   0;
aaMtmam[ 5][ 5] =   0; aaMtmam[ 5][ 6] = 274; aaMtmam[ 5][ 7] =   0; aaMtmam[ 5][ 8] = 550; aaMtmam[ 5][ 9] =   0;
aaMtmam[ 5][10] =  20; aaMtmam[ 5][11] = 242; aaMtmam[ 5][12] =  22; aaMtmam[ 5][13] =   0; aaMtmam[ 5][14] =  51;
aaMtmam[ 5][15] =  30; aaMtmam[ 5][16] =   0; aaMtmam[ 5][17] =   0; aaMtmam[ 5][18] =  54; aaMtmam[ 5][19] =  33;
aaMtmam[ 6][ 0] =   0; aaMtmam[ 6][ 1] =   0; aaMtmam[ 6][ 2] =   0; aaMtmam[ 6][ 3] = 569; aaMtmam[ 6][ 4] =   0;
aaMtmam[ 6][ 5] = 274; aaMtmam[ 6][ 6] =   0; aaMtmam[ 6][ 7] =  22; aaMtmam[ 6][ 8] =  22; aaMtmam[ 6][ 9] =   0;
aaMtmam[ 6][10] =   0; aaMtmam[ 6][11] = 215; aaMtmam[ 6][12] =   0; aaMtmam[ 6][13] =   0; aaMtmam[ 6][14] =   0;
aaMtmam[ 6][15] =  21; aaMtmam[ 6][16] =   4; aaMtmam[ 6][17] =   0; aaMtmam[ 6][18] =   0; aaMtmam[ 6][19] =  20;
aaMtmam[ 7][ 0] =  78; aaMtmam[ 7][ 1] =  18; aaMtmam[ 7][ 2] =  47; aaMtmam[ 7][ 3] =  79; aaMtmam[ 7][ 4] =   0;
aaMtmam[ 7][ 5] =   0; aaMtmam[ 7][ 6] =  22; aaMtmam[ 7][ 7] =   0; aaMtmam[ 7][ 8] =   0; aaMtmam[ 7][ 9] =   0;
aaMtmam[ 7][10] =   0; aaMtmam[ 7][11] =   0; aaMtmam[ 7][12] =   0; aaMtmam[ 7][13] =   0; aaMtmam[ 7][14] =   0;
aaMtmam[ 7][15] = 112; aaMtmam[ 7][16] =   0; aaMtmam[ 7][17] =   0; aaMtmam[ 7][18] =   1; aaMtmam[ 7][19] =   5;
aaMtmam[ 8][ 0] =   8; aaMtmam[ 8][ 1] = 232; aaMtmam[ 8][ 2] = 458; aaMtmam[ 8][ 3] =  11; aaMtmam[ 8][ 4] = 305;
aaMtmam[ 8][ 5] = 550; aaMtmam[ 8][ 6] =  22; aaMtmam[ 8][ 7] =   0; aaMtmam[ 8][ 8] =   0; aaMtmam[ 8][ 9] =   0;
aaMtmam[ 8][10] =  26; aaMtmam[ 8][11] =   0; aaMtmam[ 8][12] =   0; aaMtmam[ 8][13] =   0; aaMtmam[ 8][14] =  53;
aaMtmam[ 8][15] =  20; aaMtmam[ 8][16] =   1; aaMtmam[ 8][17] =   0; aaMtmam[ 8][18] =1525; aaMtmam[ 8][19] =   0;
aaMtmam[ 9][ 0] =  75; aaMtmam[ 9][ 1] =   0; aaMtmam[ 9][ 2] =  19; aaMtmam[ 9][ 3] =   0; aaMtmam[ 9][ 4] =  41;
aaMtmam[ 9][ 5] =   0; aaMtmam[ 9][ 6] =   0; aaMtmam[ 9][ 7] =   0; aaMtmam[ 9][ 8] =   0; aaMtmam[ 9][ 9] =   0;
aaMtmam[ 9][10] = 232; aaMtmam[ 9][11] =   6; aaMtmam[ 9][12] = 378; aaMtmam[ 9][13] =  57; aaMtmam[ 9][14] =   5;
aaMtmam[ 9][15] =   0; aaMtmam[ 9][16] = 360; aaMtmam[ 9][17] =   0; aaMtmam[ 9][18] =  16; aaMtmam[ 9][19] =2220;
aaMtmam[10][ 0] =  21; aaMtmam[10][ 1] =   6; aaMtmam[10][ 2] =   0; aaMtmam[10][ 3] =   0; aaMtmam[10][ 4] =  27;
aaMtmam[10][ 5] =  20; aaMtmam[10][ 6] =   0; aaMtmam[10][ 7] =   0; aaMtmam[10][ 8] =  26; aaMtmam[10][ 9] = 232;
aaMtmam[10][10] =   0; aaMtmam[10][11] =   4; aaMtmam[10][12] = 609; aaMtmam[10][13] = 246; aaMtmam[10][14] =  43;
aaMtmam[10][15] =  74; aaMtmam[10][16] =  34; aaMtmam[10][17] =  12; aaMtmam[10][18] =  25; aaMtmam[10][19] = 100;
aaMtmam[11][ 0] =   0; aaMtmam[11][ 1] =  50; aaMtmam[11][ 2] = 408; aaMtmam[11][ 3] =   0; aaMtmam[11][ 4] =   0;
aaMtmam[11][ 5] = 242; aaMtmam[11][ 6] = 215; aaMtmam[11][ 7] =   0; aaMtmam[11][ 8] =   0; aaMtmam[11][ 9] =   6;
aaMtmam[11][10] =   4; aaMtmam[11][11] =   0; aaMtmam[11][12] =  59; aaMtmam[11][13] =   0; aaMtmam[11][14] =  18;
aaMtmam[11][15] =  65; aaMtmam[11][16] =  50; aaMtmam[11][17] =   0; aaMtmam[11][18] =  67; aaMtmam[11][19] =   0;
aaMtmam[12][ 0] =  76; aaMtmam[12][ 1] =   0; aaMtmam[12][ 2] =  21; aaMtmam[12][ 3] =   0; aaMtmam[12][ 4] =   0;
aaMtmam[12][ 5] =  22; aaMtmam[12][ 6] =   0; aaMtmam[12][ 7] =   0; aaMtmam[12][ 8] =   0; aaMtmam[12][ 9] = 378;
aaMtmam[12][10] = 609; aaMtmam[12][11] =  59; aaMtmam[12][12] =   0; aaMtmam[12][13] =  11; aaMtmam[12][14] =   0;
aaMtmam[12][15] =  47; aaMtmam[12][16] = 691; aaMtmam[12][17] =  13; aaMtmam[12][18] =   0; aaMtmam[12][19] = 832;
aaMtmam[13][ 0] =   0; aaMtmam[13][ 1] =   0; aaMtmam[13][ 2] =   6; aaMtmam[13][ 3] =   5; aaMtmam[13][ 4] =   7;
aaMtmam[13][ 5] =   0; aaMtmam[13][ 6] =   0; aaMtmam[13][ 7] =   0; aaMtmam[13][ 8] =   0; aaMtmam[13][ 9] =  57;
aaMtmam[13][10] = 246; aaMtmam[13][11] =   0; aaMtmam[13][12] =  11; aaMtmam[13][13] =   0; aaMtmam[13][14] =  17;
aaMtmam[13][15] =  90; aaMtmam[13][16] =   8; aaMtmam[13][17] =   0; aaMtmam[13][18] = 682; aaMtmam[13][19] =   6;
aaMtmam[14][ 0] =  53; aaMtmam[14][ 1] =   9; aaMtmam[14][ 2] =  33; aaMtmam[14][ 3] =   2; aaMtmam[14][ 4] =   0;
aaMtmam[14][ 5] =  51; aaMtmam[14][ 6] =   0; aaMtmam[14][ 7] =   0; aaMtmam[14][ 8] =  53; aaMtmam[14][ 9] =   5;
aaMtmam[14][10] =  43; aaMtmam[14][11] =  18; aaMtmam[14][12] =   0; aaMtmam[14][13] =  17; aaMtmam[14][14] =   0;
aaMtmam[14][15] = 202; aaMtmam[14][16] =  78; aaMtmam[14][17] =   7; aaMtmam[14][18] =   8; aaMtmam[14][19] =   0;
aaMtmam[15][ 0] = 342; aaMtmam[15][ 1] =   3; aaMtmam[15][ 2] = 446; aaMtmam[15][ 3] =  16; aaMtmam[15][ 4] = 347;
aaMtmam[15][ 5] =  30; aaMtmam[15][ 6] =  21; aaMtmam[15][ 7] = 112; aaMtmam[15][ 8] =  20; aaMtmam[15][ 9] =   0;
aaMtmam[15][10] =  74; aaMtmam[15][11] =  65; aaMtmam[15][12] =  47; aaMtmam[15][13] =  90; aaMtmam[15][14] = 202;
aaMtmam[15][15] =   0; aaMtmam[15][16] = 614; aaMtmam[15][17] =  17; aaMtmam[15][18] = 107; aaMtmam[15][19] =   0;
aaMtmam[16][ 0] = 681; aaMtmam[16][ 1] =   0; aaMtmam[16][ 2] = 110; aaMtmam[16][ 3] =   0; aaMtmam[16][ 4] = 114;
aaMtmam[16][ 5] =   0; aaMtmam[16][ 6] =   4; aaMtmam[16][ 7] =   0; aaMtmam[16][ 8] =   1; aaMtmam[16][ 9] = 360;
aaMtmam[16][10] =  34; aaMtmam[16][11] =  50; aaMtmam[16][12] = 691; aaMtmam[16][13] =   8; aaMtmam[16][14] =  78;
aaMtmam[16][15] = 614; aaMtmam[16][16] =   0; aaMtmam[16][17] =   0; aaMtmam[16][18] =   0; aaMtmam[16][19] = 237;
aaMtmam[17][ 0] =   5; aaMtmam[17][ 1] =  16; aaMtmam[17][ 2] =   6; aaMtmam[17][ 3] =   0; aaMtmam[17][ 4] =  65;
aaMtmam[17][ 5] =   0; aaMtmam[17][ 6] =   0; aaMtmam[17][ 7] =   0; aaMtmam[17][ 8] =   0; aaMtmam[17][ 9] =   0;
aaMtmam[17][10] =  12; aaMtmam[17][11] =   0; aaMtmam[17][12] =  13; aaMtmam[17][13] =   0; aaMtmam[17][14] =   7;
aaMtmam[17][15] =  17; aaMtmam[17][16] =   0; aaMtmam[17][17] =   0; aaMtmam[17][18] =  14; aaMtmam[17][19] =   0;
aaMtmam[18][ 0] =   0; aaMtmam[18][ 1] =   0; aaMtmam[18][ 2] = 156; aaMtmam[18][ 3] =   0; aaMtmam[18][ 4] = 530;
aaMtmam[18][ 5] =  54; aaMtmam[18][ 6] =   0; aaMtmam[18][ 7] =   1; aaMtmam[18][ 8] =1525; aaMtmam[18][ 9] =  16;
aaMtmam[18][10] =  25; aaMtmam[18][11] =  67; aaMtmam[18][12] =   0; aaMtmam[18][13] = 682; aaMtmam[18][14] =   8;
aaMtmam[18][15] = 107; aaMtmam[18][16] =   0; aaMtmam[18][17] =  14; aaMtmam[18][18] =   0; aaMtmam[18][19] =   0;
aaMtmam[19][ 0] = 398; aaMtmam[19][ 1] =   0; aaMtmam[19][ 2] =   0; aaMtmam[19][ 3] =  10; aaMtmam[19][ 4] =   0;
aaMtmam[19][ 5] =  33; aaMtmam[19][ 6] =  20; aaMtmam[19][ 7] =   5; aaMtmam[19][ 8] =   0; aaMtmam[19][ 9] =2220;
aaMtmam[19][10] = 100; aaMtmam[19][11] =   0; aaMtmam[19][12] = 832; aaMtmam[19][13] =   6; aaMtmam[19][14] =   0;
aaMtmam[19][15] =   0; aaMtmam[19][16] = 237; aaMtmam[19][17] =   0; aaMtmam[19][18] =   0; aaMtmam[19][19] =   0;

mtmamPi=20*[0]
mtmamPi[ 0] = 0.0692;
mtmamPi[ 1] = 0.0184;
mtmamPi[ 2] = 0.0400;
mtmamPi[ 3] = 0.0186;
mtmamPi[ 4] = 0.0065;
mtmamPi[ 5] = 0.0238;
mtmamPi[ 6] = 0.0236;
mtmamPi[ 7] = 0.0557;
mtmamPi[ 8] = 0.0277;
mtmamPi[ 9] = 0.0905;
mtmamPi[10] = 0.1675;
mtmamPi[11] = 0.0221;
mtmamPi[12] = 0.0561;
mtmamPi[13] = 0.0611;
mtmamPi[14] = 0.0536;
mtmamPi[15] = 0.0725;
mtmamPi[16] = 0.0870;
mtmamPi[17] = 0.0293;
mtmamPi[18] = 0.0340;
mtmamPi[19] = 0.0428;

out=""
for i in range(20):
    for j in range(0,i):
        out+=str(aaMtmam[i][j])+" "
    out+="\n"

for i in range(20):
    if (i/7==i/7.0):out+="\n"
    out+=str(mtmamPi[i])+" "

out+="// this is the end of the file."
handle=open("mtmamMrBayes.dat","w")
handle.write(out)
handle.close()

#rtRev
aartREV=20*[["0"*20]]
aartREV=[i[0].split("0") for i in aartREV]
aartREV[ 0][ 0] =   0; aartREV[ 1][ 0] =  34; aartREV[ 2][ 0] =  51; aartREV[ 3][ 0] =  10; aartREV[ 4][ 0] = 439;
aartREV[ 5][ 0] =  32; aartREV[ 6][ 0] =  81; aartREV[ 7][ 0] = 135; aartREV[ 8][ 0] =  30; aartREV[ 9][ 0] =   1;
aartREV[10][ 0] =  45; aartREV[11][ 0] =  38; aartREV[12][ 0] = 235; aartREV[13][ 0] =   1; aartREV[14][ 0] =  97;
aartREV[15][ 0] = 460; aartREV[16][ 0] = 258; aartREV[17][ 0] =   5; aartREV[18][ 0] =  55; aartREV[19][ 0] = 197;
aartREV[ 0][ 1] =  34; aartREV[ 1][ 1] =   0; aartREV[ 2][ 1] =  35; aartREV[ 3][ 1] =  30; aartREV[ 4][ 1] =  92;
aartREV[ 5][ 1] = 221; aartREV[ 6][ 1] =  10; aartREV[ 7][ 1] =  41; aartREV[ 8][ 1] =  90; aartREV[ 9][ 1] =  24;
aartREV[10][ 1] =  18; aartREV[11][ 1] = 593; aartREV[12][ 1] =  57; aartREV[13][ 1] =   7; aartREV[14][ 1] =  24;
aartREV[15][ 1] = 102; aartREV[16][ 1] =  64; aartREV[17][ 1] =  13; aartREV[18][ 1] =  47; aartREV[19][ 1] =  29;
aartREV[ 0][ 2] =  51; aartREV[ 1][ 2] =  35; aartREV[ 2][ 2] =   0; aartREV[ 3][ 2] = 384; aartREV[ 4][ 2] = 128;
aartREV[ 5][ 2] = 236; aartREV[ 6][ 2] =  79; aartREV[ 7][ 2] =  94; aartREV[ 8][ 2] = 320; aartREV[ 9][ 2] =  35;
aartREV[10][ 2] =  15; aartREV[11][ 2] = 123; aartREV[12][ 2] =   1; aartREV[13][ 2] =  49; aartREV[14][ 2] =  33;
aartREV[15][ 2] = 294; aartREV[16][ 2] = 148; aartREV[17][ 2] =  16; aartREV[18][ 2] =  28; aartREV[19][ 2] =  21;
aartREV[ 0][ 3] =  10; aartREV[ 1][ 3] =  30; aartREV[ 2][ 3] = 384; aartREV[ 3][ 3] =   0; aartREV[ 4][ 3] =   1;
aartREV[ 5][ 3] =  78; aartREV[ 6][ 3] = 542; aartREV[ 7][ 3] =  61; aartREV[ 8][ 3] =  91; aartREV[ 9][ 3] =   1;
aartREV[10][ 3] =   5; aartREV[11][ 3] =  20; aartREV[12][ 3] =   1; aartREV[13][ 3] =   1; aartREV[14][ 3] =  55;
aartREV[15][ 3] = 136; aartREV[16][ 3] =  55; aartREV[17][ 3] =   1; aartREV[18][ 3] =   1; aartREV[19][ 3] =   6;
aartREV[ 0][ 4] = 439; aartREV[ 1][ 4] =  92; aartREV[ 2][ 4] = 128; aartREV[ 3][ 4] =   1; aartREV[ 4][ 4] =   0;
aartREV[ 5][ 4] =  70; aartREV[ 6][ 4] =   1; aartREV[ 7][ 4] =  48; aartREV[ 8][ 4] = 124; aartREV[ 9][ 4] = 104;
aartREV[10][ 4] = 110; aartREV[11][ 4] =  16; aartREV[12][ 4] = 156; aartREV[13][ 4] =  70; aartREV[14][ 4] =   1;
aartREV[15][ 4] =  75; aartREV[16][ 4] = 117; aartREV[17][ 4] =  55; aartREV[18][ 4] = 131; aartREV[19][ 4] = 295;
aartREV[ 0][ 5] =  32; aartREV[ 1][ 5] = 221; aartREV[ 2][ 5] = 236; aartREV[ 3][ 5] =  78; aartREV[ 4][ 5] =  70;
aartREV[ 5][ 5] =   0; aartREV[ 6][ 5] = 372; aartREV[ 7][ 5] =  18; aartREV[ 8][ 5] = 387; aartREV[ 9][ 5] =  33;
aartREV[10][ 5] =  54; aartREV[11][ 5] = 309; aartREV[12][ 5] = 158; aartREV[13][ 5] =   1; aartREV[14][ 5] =  68;
aartREV[15][ 5] = 225; aartREV[16][ 5] = 146; aartREV[17][ 5] =  10; aartREV[18][ 5] =  45; aartREV[19][ 5] =  36;
aartREV[ 0][ 6] =  81; aartREV[ 1][ 6] =  10; aartREV[ 2][ 6] =  79; aartREV[ 3][ 6] = 542; aartREV[ 4][ 6] =   1;
aartREV[ 5][ 6] = 372; aartREV[ 6][ 6] =   0; aartREV[ 7][ 6] =  70; aartREV[ 8][ 6] =  34; aartREV[ 9][ 6] =   1;
aartREV[10][ 6] =  21; aartREV[11][ 6] = 141; aartREV[12][ 6] =   1; aartREV[13][ 6] =   1; aartREV[14][ 6] =  52;
aartREV[15][ 6] =  95; aartREV[16][ 6] =  82; aartREV[17][ 6] =  17; aartREV[18][ 6] =   1; aartREV[19][ 6] =  35;
aartREV[ 0][ 7] = 135; aartREV[ 1][ 7] =  41; aartREV[ 2][ 7] =  94; aartREV[ 3][ 7] =  61; aartREV[ 4][ 7] =  48;
aartREV[ 5][ 7] =  18; aartREV[ 6][ 7] =  70; aartREV[ 7][ 7] =   0; aartREV[ 8][ 7] =  68; aartREV[ 9][ 7] =   1;
aartREV[10][ 7] =   3; aartREV[11][ 7] =  30; aartREV[12][ 7] =  37; aartREV[13][ 7] =   7; aartREV[14][ 7] =  17;
aartREV[15][ 7] = 152; aartREV[16][ 7] =   7; aartREV[17][ 7] =  23; aartREV[18][ 7] =  21; aartREV[19][ 7] =   3;
aartREV[ 0][ 8] =  30; aartREV[ 1][ 8] =  90; aartREV[ 2][ 8] = 320; aartREV[ 3][ 8] =  91; aartREV[ 4][ 8] = 124;
aartREV[ 5][ 8] = 387; aartREV[ 6][ 8] =  34; aartREV[ 7][ 8] =  68; aartREV[ 8][ 8] =   0; aartREV[ 9][ 8] =  34;
aartREV[10][ 8] =  51; aartREV[11][ 8] =  76; aartREV[12][ 8] = 116; aartREV[13][ 8] = 141; aartREV[14][ 8] =  44;
aartREV[15][ 8] = 183; aartREV[16][ 8] =  49; aartREV[17][ 8] =  48; aartREV[18][ 8] = 307; aartREV[19][ 8] =   1;
aartREV[ 0][ 9] =   1; aartREV[ 1][ 9] =  24; aartREV[ 2][ 9] =  35; aartREV[ 3][ 9] =   1; aartREV[ 4][ 9] = 104;
aartREV[ 5][ 9] =  33; aartREV[ 6][ 9] =   1; aartREV[ 7][ 9] =   1; aartREV[ 8][ 9] =  34; aartREV[ 9][ 9] =   0;
aartREV[10][ 9] = 385; aartREV[11][ 9] =  34; aartREV[12][ 9] = 375; aartREV[13][ 9] =  64; aartREV[14][ 9] =  10;
aartREV[15][ 9] =   4; aartREV[16][ 9] =  72; aartREV[17][ 9] =  39; aartREV[18][ 9] =  26; aartREV[19][ 9] =1048;
aartREV[ 0][10] =  45; aartREV[ 1][10] =  18; aartREV[ 2][10] =  15; aartREV[ 3][10] =   5; aartREV[ 4][10] = 110;
aartREV[ 5][10] =  54; aartREV[ 6][10] =  21; aartREV[ 7][10] =   3; aartREV[ 8][10] =  51; aartREV[ 9][10] = 385;
aartREV[10][10] =   0; aartREV[11][10] =  23; aartREV[12][10] = 581; aartREV[13][10] = 179; aartREV[14][10] =  22;
aartREV[15][10] =  24; aartREV[16][10] =  25; aartREV[17][10] =  47; aartREV[18][10] =  64; aartREV[19][10] = 112;
aartREV[ 0][11] =  38; aartREV[ 1][11] = 593; aartREV[ 2][11] = 123; aartREV[ 3][11] =  20; aartREV[ 4][11] =  16;
aartREV[ 5][11] = 309; aartREV[ 6][11] = 141; aartREV[ 7][11] =  30; aartREV[ 8][11] =  76; aartREV[ 9][11] =  34;
aartREV[10][11] =  23; aartREV[11][11] =   0; aartREV[12][11] = 134; aartREV[13][11] =  14; aartREV[14][11] =  43;
aartREV[15][11] =  77; aartREV[16][11] = 110; aartREV[17][11] =   6; aartREV[18][11] =   1; aartREV[19][11] =  19;
aartREV[ 0][12] = 235; aartREV[ 1][12] =  57; aartREV[ 2][12] =   1; aartREV[ 3][12] =   1; aartREV[ 4][12] = 156;
aartREV[ 5][12] = 158; aartREV[ 6][12] =   1; aartREV[ 7][12] =  37; aartREV[ 8][12] = 116; aartREV[ 9][12] = 375;
aartREV[10][12] = 581; aartREV[11][12] = 134; aartREV[12][12] =   0; aartREV[13][12] = 247; aartREV[14][12] =   1;
aartREV[15][12] =   1; aartREV[16][12] = 131; aartREV[17][12] = 111; aartREV[18][12] =  74; aartREV[19][12] = 236;
aartREV[ 0][13] =   1; aartREV[ 1][13] =   7; aartREV[ 2][13] =  49; aartREV[ 3][13] =   1; aartREV[ 4][13] =  70;
aartREV[ 5][13] =   1; aartREV[ 6][13] =   1; aartREV[ 7][13] =   7; aartREV[ 8][13] = 141; aartREV[ 9][13] =  64;
aartREV[10][13] = 179; aartREV[11][13] =  14; aartREV[12][13] = 247; aartREV[13][13] =   0; aartREV[14][13] =  11;
aartREV[15][13] =  20; aartREV[16][13] =  69; aartREV[17][13] = 182; aartREV[18][13] =1017; aartREV[19][13] =  92;
aartREV[ 0][14] =  97; aartREV[ 1][14] =  24; aartREV[ 2][14] =  33; aartREV[ 3][14] =  55; aartREV[ 4][14] =   1;
aartREV[ 5][14] =  68; aartREV[ 6][14] =  52; aartREV[ 7][14] =  17; aartREV[ 8][14] =  44; aartREV[ 9][14] =  10;
aartREV[10][14] =  22; aartREV[11][14] =  43; aartREV[12][14] =   1; aartREV[13][14] =  11; aartREV[14][14] =   0;
aartREV[15][14] = 134; aartREV[16][14] =  62; aartREV[17][14] =   9; aartREV[18][14] =  14; aartREV[19][14] =  25;
aartREV[ 0][15] = 460; aartREV[ 1][15] = 102; aartREV[ 2][15] = 294; aartREV[ 3][15] = 136; aartREV[ 4][15] =  75;
aartREV[ 5][15] = 225; aartREV[ 6][15] =  95; aartREV[ 7][15] = 152; aartREV[ 8][15] = 183; aartREV[ 9][15] =   4;
aartREV[10][15] =  24; aartREV[11][15] =  77; aartREV[12][15] =   1; aartREV[13][15] =  20; aartREV[14][15] = 134;
aartREV[15][15] =   0; aartREV[16][15] = 671; aartREV[17][15] =  14; aartREV[18][15] =  31; aartREV[19][15] =  39;
aartREV[ 0][16] = 258; aartREV[ 1][16] =  64; aartREV[ 2][16] = 148; aartREV[ 3][16] =  55; aartREV[ 4][16] = 117;
aartREV[ 5][16] = 146; aartREV[ 6][16] =  82; aartREV[ 7][16] =   7; aartREV[ 8][16] =  49; aartREV[ 9][16] =  72;
aartREV[10][16] =  25; aartREV[11][16] = 110; aartREV[12][16] = 131; aartREV[13][16] =  69; aartREV[14][16] =  62;
aartREV[15][16] = 671; aartREV[16][16] =   0; aartREV[17][16] =   1; aartREV[18][16] =  34; aartREV[19][16] = 196;
aartREV[ 0][17] =   5; aartREV[ 1][17] =  13; aartREV[ 2][17] =  16; aartREV[ 3][17] =   1; aartREV[ 4][17] =  55;
aartREV[ 5][17] =  10; aartREV[ 6][17] =  17; aartREV[ 7][17] =  23; aartREV[ 8][17] =  48; aartREV[ 9][17] =  39;
aartREV[10][17] =  47; aartREV[11][17] =   6; aartREV[12][17] = 111; aartREV[13][17] = 182; aartREV[14][17] =   9;
aartREV[15][17] =  14; aartREV[16][17] =   1; aartREV[17][17] =   0; aartREV[18][17] = 176; aartREV[19][17] =  26;
aartREV[ 0][18] =  55; aartREV[ 1][18] =  47; aartREV[ 2][18] =  28; aartREV[ 3][18] =   1; aartREV[ 4][18] = 131;
aartREV[ 5][18] =  45; aartREV[ 6][18] =   1; aartREV[ 7][18] =  21; aartREV[ 8][18] = 307; aartREV[ 9][18] =  26;
aartREV[10][18] =  64; aartREV[11][18] =   1; aartREV[12][18] =  74; aartREV[13][18] =1017; aartREV[14][18] =  14;
aartREV[15][18] =  31; aartREV[16][18] =  34; aartREV[17][18] = 176; aartREV[18][18] =   0; aartREV[19][18] =  59;
aartREV[ 0][19] = 197; aartREV[ 1][19] =  29; aartREV[ 2][19] =  21; aartREV[ 3][19] =   6; aartREV[ 4][19] = 295;
aartREV[ 5][19] =  36; aartREV[ 6][19] =  35; aartREV[ 7][19] =   3; aartREV[ 8][19] =   1; aartREV[ 9][19] =1048;
aartREV[10][19] = 112; aartREV[11][19] =  19; aartREV[12][19] = 236; aartREV[13][19] =  92; aartREV[14][19] =  25;
aartREV[15][19] =  39; aartREV[16][19] = 196; aartREV[17][19] =  26; aartREV[18][19] =  59; aartREV[19][19] =   0;

rtrevPi=20*[0]
rtrevPi[ 0] = 0.0646;
rtrevPi[ 1] = 0.0453;
rtrevPi[ 2] = 0.0376;
rtrevPi[ 3] = 0.0422;
rtrevPi[ 4] = 0.0114;
rtrevPi[ 5] = 0.0606;
rtrevPi[ 6] = 0.0607;
rtrevPi[ 7] = 0.0639;
rtrevPi[ 8] = 0.0273;
rtrevPi[ 9] = 0.0679;
rtrevPi[10] = 0.1018;
rtrevPi[11] = 0.0751;
rtrevPi[12] = 0.0150;
rtrevPi[13] = 0.0287;
rtrevPi[14] = 0.0681;
rtrevPi[15] = 0.0488;
rtrevPi[16] = 0.0622;
rtrevPi[17] = 0.0251;
rtrevPi[18] = 0.0318;
rtrevPi[19] = 0.0619;

out=""
for i in range(20):
    for j in range(0,i):
        out+=str(aartREV[i][j])+" "
    out+="\n"

for i in range(20):
    if (i/7==i/7.0):out+="\n"
    out+=str(rtrevPi[i])+" "

out+="// this is the end of the file."
handle=open("rtrevMrBayes.dat","w")
handle.write(out)
handle.close()

#wag
aaWAG=20*[["0"*20]]
aaWAG=[i[0].split("0") for i in aaWAG]
aaWAG[ 0][ 0] = 0.0000000; aaWAG[ 1][ 0] = 0.5515710; aaWAG[ 2][ 0] = 0.5098480; aaWAG[ 3][ 0] = 0.7389980; aaWAG[ 4][ 0] = 1.0270400; 
aaWAG[ 5][ 0] = 0.9085980; aaWAG[ 6][ 0] = 1.5828500; aaWAG[ 7][ 0] = 1.4167200; aaWAG[ 8][ 0] = 0.3169540; aaWAG[ 9][ 0] = 0.1933350; 
aaWAG[10][ 0] = 0.3979150; aaWAG[11][ 0] = 0.9062650; aaWAG[12][ 0] = 0.8934960; aaWAG[13][ 0] = 0.2104940; aaWAG[14][ 0] = 1.4385500; 
aaWAG[15][ 0] = 3.3707900; aaWAG[16][ 0] = 2.1211100; aaWAG[17][ 0] = 0.1131330; aaWAG[18][ 0] = 0.2407350; aaWAG[19][ 0] = 2.0060100;
aaWAG[ 0][ 1] = 0.5515710; aaWAG[ 1][ 1] = 0.0000000; aaWAG[ 2][ 1] = 0.6353460; aaWAG[ 3][ 1] = 0.1473040; aaWAG[ 4][ 1] = 0.5281910;  
aaWAG[ 5][ 1] = 3.0355000; aaWAG[ 6][ 1] = 0.4391570; aaWAG[ 7][ 1] = 0.5846650; aaWAG[ 8][ 1] = 2.1371500; aaWAG[ 9][ 1] = 0.1869790;  
aaWAG[10][ 1] = 0.4976710; aaWAG[11][ 1] = 5.3514200; aaWAG[12][ 1] = 0.6831620; aaWAG[13][ 1] = 0.1027110; aaWAG[14][ 1] = 0.6794890;  
aaWAG[15][ 1] = 1.2241900; aaWAG[16][ 1] = 0.5544130; aaWAG[17][ 1] = 1.1639200; aaWAG[18][ 1] = 0.3815330; aaWAG[19][ 1] = 0.2518490;
aaWAG[ 0][ 2] = 0.5098480; aaWAG[ 1][ 2] = 0.6353460; aaWAG[ 2][ 2] = 0.0000000; aaWAG[ 3][ 2] = 5.4294200; aaWAG[ 4][ 2] = 0.2652560;  
aaWAG[ 5][ 2] = 1.5436400; aaWAG[ 6][ 2] = 0.9471980; aaWAG[ 7][ 2] = 1.1255600; aaWAG[ 8][ 2] = 3.9562900; aaWAG[ 9][ 2] = 0.5542360;  
aaWAG[10][ 2] = 0.1315280; aaWAG[11][ 2] = 3.0120100; aaWAG[12][ 2] = 0.1982210; aaWAG[13][ 2] = 0.0961621; aaWAG[14][ 2] = 0.1950810;  
aaWAG[15][ 2] = 3.9742300; aaWAG[16][ 2] = 2.0300600; aaWAG[17][ 2] = 0.0719167; aaWAG[18][ 2] = 1.0860000; aaWAG[19][ 2] = 0.1962460;
aaWAG[ 0][ 3] = 0.7389980; aaWAG[ 1][ 3] = 0.1473040; aaWAG[ 2][ 3] = 5.4294200; aaWAG[ 3][ 3] = 0.0000000; aaWAG[ 4][ 3] = 0.0302949;  
aaWAG[ 5][ 3] = 0.6167830; aaWAG[ 6][ 3] = 6.1741600; aaWAG[ 7][ 3] = 0.8655840; aaWAG[ 8][ 3] = 0.9306760; aaWAG[ 9][ 3] = 0.0394370;  
aaWAG[10][ 3] = 0.0848047; aaWAG[11][ 3] = 0.4798550; aaWAG[12][ 3] = 0.1037540; aaWAG[13][ 3] = 0.0467304; aaWAG[14][ 3] = 0.4239840;  
aaWAG[15][ 3] = 1.0717600; aaWAG[16][ 3] = 0.3748660; aaWAG[17][ 3] = 0.1297670; aaWAG[18][ 3] = 0.3257110; aaWAG[19][ 3] = 0.1523350;
aaWAG[ 0][ 4] = 1.0270400; aaWAG[ 1][ 4] = 0.5281910; aaWAG[ 2][ 4] = 0.2652560; aaWAG[ 3][ 4] = 0.0302949; aaWAG[ 4][ 4] = 0.0000000;  
aaWAG[ 5][ 4] = 0.0988179; aaWAG[ 6][ 4] = 0.0213520; aaWAG[ 7][ 4] = 0.3066740; aaWAG[ 8][ 4] = 0.2489720; aaWAG[ 9][ 4] = 0.1701350;  
aaWAG[10][ 4] = 0.3842870; aaWAG[11][ 4] = 0.0740339; aaWAG[12][ 4] = 0.3904820; aaWAG[13][ 4] = 0.3980200; aaWAG[14][ 4] = 0.1094040;  
aaWAG[15][ 4] = 1.4076600; aaWAG[16][ 4] = 0.5129840; aaWAG[17][ 4] = 0.7170700; aaWAG[18][ 4] = 0.5438330; aaWAG[19][ 4] = 1.0021400;
aaWAG[ 0][ 5] = 0.9085980; aaWAG[ 1][ 5] = 3.0355000; aaWAG[ 2][ 5] = 1.5436400; aaWAG[ 3][ 5] = 0.6167830; aaWAG[ 4][ 5] = 0.0988179;  
aaWAG[ 5][ 5] = 0.0000000; aaWAG[ 6][ 5] = 5.4694700; aaWAG[ 7][ 5] = 0.3300520; aaWAG[ 8][ 5] = 4.2941100; aaWAG[ 9][ 5] = 0.1139170;  
aaWAG[10][ 5] = 0.8694890; aaWAG[11][ 5] = 3.8949000; aaWAG[12][ 5] = 1.5452600; aaWAG[13][ 5] = 0.0999208; aaWAG[14][ 5] = 0.9333720;  
aaWAG[15][ 5] = 1.0288700; aaWAG[16][ 5] = 0.8579280; aaWAG[17][ 5] = 0.2157370; aaWAG[18][ 5] = 0.2277100; aaWAG[19][ 5] = 0.3012810;
aaWAG[ 0][ 6] = 1.5828500; aaWAG[ 1][ 6] = 0.4391570; aaWAG[ 2][ 6] = 0.9471980; aaWAG[ 3][ 6] = 6.1741600; aaWAG[ 4][ 6] = 0.0213520;  
aaWAG[ 5][ 6] = 5.4694700; aaWAG[ 6][ 6] = 0.0000000; aaWAG[ 7][ 6] = 0.5677170; aaWAG[ 8][ 6] = 0.5700250; aaWAG[ 9][ 6] = 0.1273950;  
aaWAG[10][ 6] = 0.1542630; aaWAG[11][ 6] = 2.5844300; aaWAG[12][ 6] = 0.3151240; aaWAG[13][ 6] = 0.0811339; aaWAG[14][ 6] = 0.6823550;  
aaWAG[15][ 6] = 0.7049390; aaWAG[16][ 6] = 0.8227650; aaWAG[17][ 6] = 0.1565570; aaWAG[18][ 6] = 0.1963030; aaWAG[19][ 6] = 0.5887310;
aaWAG[ 0][ 7] = 1.4167200; aaWAG[ 1][ 7] = 0.5846650; aaWAG[ 2][ 7] = 1.1255600; aaWAG[ 3][ 7] = 0.8655840; aaWAG[ 4][ 7] = 0.3066740;  
aaWAG[ 5][ 7] = 0.3300520; aaWAG[ 6][ 7] = 0.5677170; aaWAG[ 7][ 7] = 0.0000000; aaWAG[ 8][ 7] = 0.2494100; aaWAG[ 9][ 7] = 0.0304501;  
aaWAG[10][ 7] = 0.0613037; aaWAG[11][ 7] = 0.3735580; aaWAG[12][ 7] = 0.1741000; aaWAG[13][ 7] = 0.0499310; aaWAG[14][ 7] = 0.2435700;  
aaWAG[15][ 7] = 1.3418200; aaWAG[16][ 7] = 0.2258330; aaWAG[17][ 7] = 0.3369830; aaWAG[18][ 7] = 0.1036040; aaWAG[19][ 7] = 0.1872470;
aaWAG[ 0][ 8] = 0.3169540; aaWAG[ 1][ 8] = 2.1371500; aaWAG[ 2][ 8] = 3.9562900; aaWAG[ 3][ 8] = 0.9306760; aaWAG[ 4][ 8] = 0.2489720;  
aaWAG[ 5][ 8] = 4.2941100; aaWAG[ 6][ 8] = 0.5700250; aaWAG[ 7][ 8] = 0.2494100; aaWAG[ 8][ 8] = 0.0000000; aaWAG[ 9][ 8] = 0.1381900;  
aaWAG[10][ 8] = 0.4994620; aaWAG[11][ 8] = 0.8904320; aaWAG[12][ 8] = 0.4041410; aaWAG[13][ 8] = 0.6793710; aaWAG[14][ 8] = 0.6961980;  
aaWAG[15][ 8] = 0.7401690; aaWAG[16][ 8] = 0.4733070; aaWAG[17][ 8] = 0.2625690; aaWAG[18][ 8] = 3.8734400; aaWAG[19][ 8] = 0.1183580;
aaWAG[ 0][ 9] = 0.1933350; aaWAG[ 1][ 9] = 0.1869790; aaWAG[ 2][ 9] = 0.5542360; aaWAG[ 3][ 9] = 0.0394370; aaWAG[ 4][ 9] = 0.1701350;  
aaWAG[ 5][ 9] = 0.1139170; aaWAG[ 6][ 9] = 0.1273950; aaWAG[ 7][ 9] = 0.0304501; aaWAG[ 8][ 9] = 0.1381900; aaWAG[ 9][ 9] = 0.0000000;  
aaWAG[10][ 9] = 3.1709700; aaWAG[11][ 9] = 0.3238320; aaWAG[12][ 9] = 4.2574600; aaWAG[13][ 9] = 1.0594700; aaWAG[14][ 9] = 0.0999288;  
aaWAG[15][ 9] = 0.3194400; aaWAG[16][ 9] = 1.4581600; aaWAG[17][ 9] = 0.2124830; aaWAG[18][ 9] = 0.4201700; aaWAG[19][ 9] = 7.8213000;
aaWAG[ 0][10] = 0.3979150; aaWAG[ 1][10] = 0.4976710; aaWAG[ 2][10] = 0.1315280; aaWAG[ 3][10] = 0.0848047; aaWAG[ 4][10] = 0.3842870;  
aaWAG[ 5][10] = 0.8694890; aaWAG[ 6][10] = 0.1542630; aaWAG[ 7][10] = 0.0613037; aaWAG[ 8][10] = 0.4994620; aaWAG[ 9][10] = 3.1709700;  
aaWAG[10][10] = 0.0000000; aaWAG[11][10] = 0.2575550; aaWAG[12][10] = 4.8540200; aaWAG[13][10] = 2.1151700; aaWAG[14][10] = 0.4158440;  
aaWAG[15][10] = 0.3447390; aaWAG[16][10] = 0.3266220; aaWAG[17][10] = 0.6653090; aaWAG[18][10] = 0.3986180; aaWAG[19][10] = 1.8003400;
aaWAG[ 0][11] = 0.9062650; aaWAG[ 1][11] = 5.3514200; aaWAG[ 2][11] = 3.0120100; aaWAG[ 3][11] = 0.4798550; aaWAG[ 4][11] = 0.0740339;  
aaWAG[ 5][11] = 3.8949000; aaWAG[ 6][11] = 2.5844300; aaWAG[ 7][11] = 0.3735580; aaWAG[ 8][11] = 0.8904320; aaWAG[ 9][11] = 0.3238320;  
aaWAG[10][11] = 0.2575550; aaWAG[11][11] = 0.0000000; aaWAG[12][11] = 0.9342760; aaWAG[13][11] = 0.0888360; aaWAG[14][11] = 0.5568960;  
aaWAG[15][11] = 0.9671300; aaWAG[16][11] = 1.3869800; aaWAG[17][11] = 0.1375050; aaWAG[18][11] = 0.1332640; aaWAG[19][11] = 0.3054340;
aaWAG[ 0][12] = 0.8934960; aaWAG[ 1][12] = 0.6831620; aaWAG[ 2][12] = 0.1982210; aaWAG[ 3][12] = 0.1037540; aaWAG[ 4][12] = 0.3904820;  
aaWAG[ 5][12] = 1.5452600; aaWAG[ 6][12] = 0.3151240; aaWAG[ 7][12] = 0.1741000; aaWAG[ 8][12] = 0.4041410; aaWAG[ 9][12] = 4.2574600;  
aaWAG[10][12] = 4.8540200; aaWAG[11][12] = 0.9342760; aaWAG[12][12] = 0.0000000; aaWAG[13][12] = 1.1906300; aaWAG[14][12] = 0.1713290;  
aaWAG[15][12] = 0.4939050; aaWAG[16][12] = 1.5161200; aaWAG[17][12] = 0.5157060; aaWAG[18][12] = 0.4284370; aaWAG[19][12] = 2.0584500;
aaWAG[ 0][13] = 0.2104940; aaWAG[ 1][13] = 0.1027110; aaWAG[ 2][13] = 0.0961621; aaWAG[ 3][13] = 0.0467304; aaWAG[ 4][13] = 0.3980200;  
aaWAG[ 5][13] = 0.0999208; aaWAG[ 6][13] = 0.0811339; aaWAG[ 7][13] = 0.0499310; aaWAG[ 8][13] = 0.6793710; aaWAG[ 9][13] = 1.0594700;  
aaWAG[10][13] = 2.1151700; aaWAG[11][13] = 0.0888360; aaWAG[12][13] = 1.1906300; aaWAG[13][13] = 0.0000000; aaWAG[14][13] = 0.1614440;  
aaWAG[15][13] = 0.5459310; aaWAG[16][13] = 0.1719030; aaWAG[17][13] = 1.5296400; aaWAG[18][13] = 6.4542800; aaWAG[19][13] = 0.6498920;
aaWAG[ 0][14] = 1.4385500; aaWAG[ 1][14] = 0.6794890; aaWAG[ 2][14] = 0.1950810; aaWAG[ 3][14] = 0.4239840; aaWAG[ 4][14] = 0.1094040;  
aaWAG[ 5][14] = 0.9333720; aaWAG[ 6][14] = 0.6823550; aaWAG[ 7][14] = 0.2435700; aaWAG[ 8][14] = 0.6961980; aaWAG[ 9][14] = 0.0999288;  
aaWAG[10][14] = 0.4158440; aaWAG[11][14] = 0.5568960; aaWAG[12][14] = 0.1713290; aaWAG[13][14] = 0.1614440; aaWAG[14][14] = 0.0000000;  
aaWAG[15][14] = 1.6132800; aaWAG[16][14] = 0.7953840; aaWAG[17][14] = 0.1394050; aaWAG[18][14] = 0.2160460; aaWAG[19][14] = 0.3148870;
aaWAG[ 0][15] = 3.3707900; aaWAG[ 1][15] = 1.2241900; aaWAG[ 2][15] = 3.9742300; aaWAG[ 3][15] = 1.0717600; aaWAG[ 4][15] = 1.4076600;  
aaWAG[ 5][15] = 1.0288700; aaWAG[ 6][15] = 0.7049390; aaWAG[ 7][15] = 1.3418200; aaWAG[ 8][15] = 0.7401690; aaWAG[ 9][15] = 0.3194400;  
aaWAG[10][15] = 0.3447390; aaWAG[11][15] = 0.9671300; aaWAG[12][15] = 0.4939050; aaWAG[13][15] = 0.5459310; aaWAG[14][15] = 1.6132800;  
aaWAG[15][15] = 0.0000000; aaWAG[16][15] = 4.3780200; aaWAG[17][15] = 0.5237420; aaWAG[18][15] = 0.7869930; aaWAG[19][15] = 0.2327390;
aaWAG[ 0][16] = 2.1211100; aaWAG[ 1][16] = 0.5544130; aaWAG[ 2][16] = 2.0300600; aaWAG[ 3][16] = 0.3748660; aaWAG[ 4][16] = 0.5129840;  
aaWAG[ 5][16] = 0.8579280; aaWAG[ 6][16] = 0.8227650; aaWAG[ 7][16] = 0.2258330; aaWAG[ 8][16] = 0.4733070; aaWAG[ 9][16] = 1.4581600;  
aaWAG[10][16] = 0.3266220; aaWAG[11][16] = 1.3869800; aaWAG[12][16] = 1.5161200; aaWAG[13][16] = 0.1719030; aaWAG[14][16] = 0.7953840;  
aaWAG[15][16] = 4.3780200; aaWAG[16][16] = 0.0000000; aaWAG[17][16] = 0.1108640; aaWAG[18][16] = 0.2911480; aaWAG[19][16] = 1.3882300;
aaWAG[ 0][17] = 0.1131330; aaWAG[ 1][17] = 1.1639200; aaWAG[ 2][17] = 0.0719167; aaWAG[ 3][17] = 0.1297670; aaWAG[ 4][17] = 0.7170700;  
aaWAG[ 5][17] = 0.2157370; aaWAG[ 6][17] = 0.1565570; aaWAG[ 7][17] = 0.3369830; aaWAG[ 8][17] = 0.2625690; aaWAG[ 9][17] = 0.2124830;  
aaWAG[10][17] = 0.6653090; aaWAG[11][17] = 0.1375050; aaWAG[12][17] = 0.5157060; aaWAG[13][17] = 1.5296400; aaWAG[14][17] = 0.1394050;  
aaWAG[15][17] = 0.5237420; aaWAG[16][17] = 0.1108640; aaWAG[17][17] = 0.0000000; aaWAG[18][17] = 2.4853900; aaWAG[19][17] = 0.3653690;
aaWAG[ 0][18] = 0.2407350; aaWAG[ 1][18] = 0.3815330; aaWAG[ 2][18] = 1.0860000; aaWAG[ 3][18] = 0.3257110; aaWAG[ 4][18] = 0.5438330;  
aaWAG[ 5][18] = 0.2277100; aaWAG[ 6][18] = 0.1963030; aaWAG[ 7][18] = 0.1036040; aaWAG[ 8][18] = 3.8734400; aaWAG[ 9][18] = 0.4201700;  
aaWAG[10][18] = 0.3986180; aaWAG[11][18] = 0.1332640; aaWAG[12][18] = 0.4284370; aaWAG[13][18] = 6.4542800; aaWAG[14][18] = 0.2160460;  
aaWAG[15][18] = 0.7869930; aaWAG[16][18] = 0.2911480; aaWAG[17][18] = 2.4853900; aaWAG[18][18] = 0.0000000; aaWAG[19][18] = 0.3147300;
aaWAG[ 0][19] = 2.0060100; aaWAG[ 1][19] = 0.2518490; aaWAG[ 2][19] = 0.1962460; aaWAG[ 3][19] = 0.1523350; aaWAG[ 4][19] = 1.0021400;  
aaWAG[ 5][19] = 0.3012810; aaWAG[ 6][19] = 0.5887310; aaWAG[ 7][19] = 0.1872470; aaWAG[ 8][19] = 0.1183580; aaWAG[ 9][19] = 7.8213000;  
aaWAG[10][19] = 1.8003400; aaWAG[11][19] = 0.3054340; aaWAG[12][19] = 2.0584500; aaWAG[13][19] = 0.6498920; aaWAG[14][19] = 0.3148870;  
aaWAG[15][19] = 0.2327390; aaWAG[16][19] = 1.3882300; aaWAG[17][19] = 0.3653690; aaWAG[18][19] = 0.3147300; aaWAG[19][19] = 0.0000000;

wagPi=20*[0]
wagPi[ 0] = 0.08662790;
wagPi[ 1] = 0.04397200;
wagPi[ 2] = 0.03908940;
wagPi[ 3] = 0.05704510;
wagPi[ 4] = 0.01930780;
wagPi[ 5] = 0.03672810;
wagPi[ 6] = 0.05805890;
wagPi[ 7] = 0.08325180;
wagPi[ 8] = 0.02443130;
wagPi[ 9] = 0.04846600;
wagPi[10] = 0.08620970;
wagPi[11] = 0.06202860;
wagPi[12] = 0.01950273;
wagPi[13] = 0.03843190;
wagPi[14] = 0.04576310;
wagPi[15] = 0.06951790;
wagPi[16] = 0.06101270;
wagPi[17] = 0.01438590;
wagPi[18] = 0.03527420;
wagPi[19] = 0.07089560;

out=""
for i in range(20):
    for j in range(0,i):
        out+=str(aaWAG[i][j])+" "
    out+="\n"

for i in range(20):
    if (i/7==i/7.0):out+="\n"
    out+=str(wagPi[i])+" "

out+="// this is the end of the file."
handle=open("wagMrBayes.dat","w")
handle.write(out)
handle.close()

#cpRev
aacpREV=20*[["0"*20]]
aacpREV=[i[0].split("0") for i in aacpREV]
aacpREV[ 0][ 0] =    0; aacpREV[ 0][ 1] =  105; aacpREV[ 0][ 2] =  227; aacpREV[ 0][ 3] =  175; aacpREV[ 0][ 4] =  669; 
aacpREV[ 0][ 5] =  157; aacpREV[ 0][ 6] =  499; aacpREV[ 0][ 7] =  665; aacpREV[ 0][ 8] =   66; aacpREV[ 0][ 9] =  145; 
aacpREV[ 0][10] =  197; aacpREV[ 0][11] =  236; aacpREV[ 0][12] =  185; aacpREV[ 0][13] =   68; aacpREV[ 0][14] =  490; 
aacpREV[ 0][15] = 2440; aacpREV[ 0][16] = 1340; aacpREV[ 0][17] =   14; aacpREV[ 0][18] =   56; aacpREV[ 0][19] =  968; 
aacpREV[ 1][ 0] =  105; aacpREV[ 1][ 1] =    0; aacpREV[ 1][ 2] =  357; aacpREV[ 1][ 3] =   43; aacpREV[ 1][ 4] =  823; 
aacpREV[ 1][ 5] = 1745; aacpREV[ 1][ 6] =  152; aacpREV[ 1][ 7] =  243; aacpREV[ 1][ 8] =  715; aacpREV[ 1][ 9] =  136; 
aacpREV[ 1][10] =  203; aacpREV[ 1][11] = 4482; aacpREV[ 1][12] =  125; aacpREV[ 1][13] =   53; aacpREV[ 1][14] =   87; 
aacpREV[ 1][15] =  385; aacpREV[ 1][16] =  314; aacpREV[ 1][17] =  230; aacpREV[ 1][18] =  323; aacpREV[ 1][19] =   92; 
aacpREV[ 2][ 0] =  227; aacpREV[ 2][ 1] =  357; aacpREV[ 2][ 2] =    0; aacpREV[ 2][ 3] = 4435; aacpREV[ 2][ 4] =  538; 
aacpREV[ 2][ 5] =  768; aacpREV[ 2][ 6] = 1055; aacpREV[ 2][ 7] =  653; aacpREV[ 2][ 8] = 1405; aacpREV[ 2][ 9] =  168; 
aacpREV[ 2][10] =  113; aacpREV[ 2][11] = 2430; aacpREV[ 2][12] =   61; aacpREV[ 2][13] =   97; aacpREV[ 2][14] =  173; 
aacpREV[ 2][15] = 2085; aacpREV[ 2][16] = 1393; aacpREV[ 2][17] =   40; aacpREV[ 2][18] =  754; aacpREV[ 2][19] =   83; 
aacpREV[ 3][ 0] =  175; aacpREV[ 3][ 1] =   43; aacpREV[ 3][ 2] = 4435; aacpREV[ 3][ 3] =    0; aacpREV[ 3][ 4] =   10; 
aacpREV[ 3][ 5] =  400; aacpREV[ 3][ 6] = 3691; aacpREV[ 3][ 7] =  431; aacpREV[ 3][ 8] =  331; aacpREV[ 3][ 9] =   10; 
aacpREV[ 3][10] =   10; aacpREV[ 3][11] =  412; aacpREV[ 3][12] =   47; aacpREV[ 3][13] =   22; aacpREV[ 3][14] =  170; 
aacpREV[ 3][15] =  590; aacpREV[ 3][16] =  266; aacpREV[ 3][17] =   18; aacpREV[ 3][18] =  281; aacpREV[ 3][19] =   75; 
aacpREV[ 4][ 0] =  669; aacpREV[ 4][ 1] =  823; aacpREV[ 4][ 2] =  538; aacpREV[ 4][ 3] =   10; aacpREV[ 4][ 4] =    0; 
aacpREV[ 4][ 5] =   10; aacpREV[ 4][ 6] =   10; aacpREV[ 4][ 7] =  303; aacpREV[ 4][ 8] =  441; aacpREV[ 4][ 9] =  280; 
aacpREV[ 4][10] =  396; aacpREV[ 4][11] =   48; aacpREV[ 4][12] =  159; aacpREV[ 4][13] =  726; aacpREV[ 4][14] =  285; 
aacpREV[ 4][15] = 2331; aacpREV[ 4][16] =  576; aacpREV[ 4][17] =  435; aacpREV[ 4][18] = 1466; aacpREV[ 4][19] =  592; 
aacpREV[ 5][ 0] =  157; aacpREV[ 5][ 1] = 1745; aacpREV[ 5][ 2] =  768; aacpREV[ 5][ 3] =  400; aacpREV[ 5][ 4] =   10; 
aacpREV[ 5][ 5] =    0; aacpREV[ 5][ 6] = 3122; aacpREV[ 5][ 7] =  133; aacpREV[ 5][ 8] = 1269; aacpREV[ 5][ 9] =   92; 
aacpREV[ 5][10] =  286; aacpREV[ 5][11] = 3313; aacpREV[ 5][12] =  202; aacpREV[ 5][13] =   10; aacpREV[ 5][14] =  323; 
aacpREV[ 5][15] =  396; aacpREV[ 5][16] =  241; aacpREV[ 5][17] =   53; aacpREV[ 5][18] =  391; aacpREV[ 5][19] =   54; 
aacpREV[ 6][ 0] =  499; aacpREV[ 6][ 1] =  152; aacpREV[ 6][ 2] = 1055; aacpREV[ 6][ 3] = 3691; aacpREV[ 6][ 4] =   10; 
aacpREV[ 6][ 5] = 3122; aacpREV[ 6][ 6] =    0; aacpREV[ 6][ 7] =  379; aacpREV[ 6][ 8] =  162; aacpREV[ 6][ 9] =  148; 
aacpREV[ 6][10] =   82; aacpREV[ 6][11] = 2629; aacpREV[ 6][12] =  113; aacpREV[ 6][13] =  145; aacpREV[ 6][14] =  185; 
aacpREV[ 6][15] =  568; aacpREV[ 6][16] =  369; aacpREV[ 6][17] =   63; aacpREV[ 6][18] =  142; aacpREV[ 6][19] =  200; 
aacpREV[ 7][ 0] =  665; aacpREV[ 7][ 1] =  243; aacpREV[ 7][ 2] =  653; aacpREV[ 7][ 3] =  431; aacpREV[ 7][ 4] =  303; 
aacpREV[ 7][ 5] =  133; aacpREV[ 7][ 6] =  379; aacpREV[ 7][ 7] =    0; aacpREV[ 7][ 8] =   19; aacpREV[ 7][ 9] =   40; 
aacpREV[ 7][10] =   20; aacpREV[ 7][11] =  263; aacpREV[ 7][12] =   21; aacpREV[ 7][13] =   25; aacpREV[ 7][14] =   28; 
aacpREV[ 7][15] =  691; aacpREV[ 7][16] =   92; aacpREV[ 7][17] =   82; aacpREV[ 7][18] =   10; aacpREV[ 7][19] =   91; 
aacpREV[ 8][ 0] =   66; aacpREV[ 8][ 1] =  715; aacpREV[ 8][ 2] = 1405; aacpREV[ 8][ 3] =  331; aacpREV[ 8][ 4] =  441; 
aacpREV[ 8][ 5] = 1269; aacpREV[ 8][ 6] =  162; aacpREV[ 8][ 7] =   19; aacpREV[ 8][ 8] =    0; aacpREV[ 8][ 9] =   29; 
aacpREV[ 8][10] =   66; aacpREV[ 8][11] =  305; aacpREV[ 8][12] =   10; aacpREV[ 8][13] =  127; aacpREV[ 8][14] =  152; 
aacpREV[ 8][15] =  303; aacpREV[ 8][16] =   32; aacpREV[ 8][17] =   69; aacpREV[ 8][18] = 1971; aacpREV[ 8][19] =   25; 
aacpREV[ 9][ 0] =  145; aacpREV[ 9][ 1] =  136; aacpREV[ 9][ 2] =  168; aacpREV[ 9][ 3] =   10; aacpREV[ 9][ 4] =  280; 
aacpREV[ 9][ 5] =   92; aacpREV[ 9][ 6] =  148; aacpREV[ 9][ 7] =   40; aacpREV[ 9][ 8] =   29; aacpREV[ 9][ 9] =    0; 
aacpREV[ 9][10] = 1745; aacpREV[ 9][11] =  345; aacpREV[ 9][12] = 1772; aacpREV[ 9][13] =  454; aacpREV[ 9][14] =  117; 
aacpREV[ 9][15] =  216; aacpREV[ 9][16] = 1040; aacpREV[ 9][17] =   42; aacpREV[ 9][18] =   89; aacpREV[ 9][19] = 4797; 
aacpREV[10][ 0] =  197; aacpREV[10][ 1] =  203; aacpREV[10][ 2] =  113; aacpREV[10][ 3] =   10; aacpREV[10][ 4] =  396; 
aacpREV[10][ 5] =  286; aacpREV[10][ 6] =   82; aacpREV[10][ 7] =   20; aacpREV[10][ 8] =   66; aacpREV[10][ 9] = 1745; 
aacpREV[10][10] =    0; aacpREV[10][11] =  218; aacpREV[10][12] = 1351; aacpREV[10][13] = 1268; aacpREV[10][14] =  219; 
aacpREV[10][15] =  516; aacpREV[10][16] =  156; aacpREV[10][17] =  159; aacpREV[10][18] =  189; aacpREV[10][19] =  865; 
aacpREV[11][ 0] =  236; aacpREV[11][ 1] = 4482; aacpREV[11][ 2] = 2430; aacpREV[11][ 3] =  412; aacpREV[11][ 4] =   48; 
aacpREV[11][ 5] = 3313; aacpREV[11][ 6] = 2629; aacpREV[11][ 7] =  263; aacpREV[11][ 8] =  305; aacpREV[11][ 9] =  345; 
aacpREV[11][10] =  218; aacpREV[11][11] =    0; aacpREV[11][12] =  193; aacpREV[11][13] =   72; aacpREV[11][14] =  302; 
aacpREV[11][15] =  868; aacpREV[11][16] =  918; aacpREV[11][17] =   10; aacpREV[11][18] =  247; aacpREV[11][19] =  249; 
aacpREV[12][ 0] =  185; aacpREV[12][ 1] =  125; aacpREV[12][ 2] =   61; aacpREV[12][ 3] =   47; aacpREV[12][ 4] =  159; 
aacpREV[12][ 5] =  202; aacpREV[12][ 6] =  113; aacpREV[12][ 7] =   21; aacpREV[12][ 8] =   10; aacpREV[12][ 9] = 1772; 
aacpREV[12][10] = 1351; aacpREV[12][11] =  193; aacpREV[12][12] =    0; aacpREV[12][13] =  327; aacpREV[12][14] =  100; 
aacpREV[12][15] =   93; aacpREV[12][16] =  645; aacpREV[12][17] =   86; aacpREV[12][18] =  215; aacpREV[12][19] =  475; 
aacpREV[13][ 0] =   68; aacpREV[13][ 1] =   53; aacpREV[13][ 2] =   97; aacpREV[13][ 3] =   22; aacpREV[13][ 4] =  726; 
aacpREV[13][ 5] =   10; aacpREV[13][ 6] =  145; aacpREV[13][ 7] =   25; aacpREV[13][ 8] =  127; aacpREV[13][ 9] =  454; 
aacpREV[13][10] = 1268; aacpREV[13][11] =   72; aacpREV[13][12] =  327; aacpREV[13][13] =    0; aacpREV[13][14] =   43; 
aacpREV[13][15] =  487; aacpREV[13][16] =  148; aacpREV[13][17] =  468; aacpREV[13][18] = 2370; aacpREV[13][19] =  317; 
aacpREV[14][ 0] =  490; aacpREV[14][ 1] =   87; aacpREV[14][ 2] =  173; aacpREV[14][ 3] =  170; aacpREV[14][ 4] =  285; 
aacpREV[14][ 5] =  323; aacpREV[14][ 6] =  185; aacpREV[14][ 7] =   28; aacpREV[14][ 8] =  152; aacpREV[14][ 9] =  117; 
aacpREV[14][10] =  219; aacpREV[14][11] =  302; aacpREV[14][12] =  100; aacpREV[14][13] =   43; aacpREV[14][14] =    0; 
aacpREV[14][15] = 1202; aacpREV[14][16] =  260; aacpREV[14][17] =   49; aacpREV[14][18] =   97; aacpREV[14][19] =  122; 
aacpREV[15][ 0] = 2440; aacpREV[15][ 1] =  385; aacpREV[15][ 2] = 2085; aacpREV[15][ 3] =  590; aacpREV[15][ 4] = 2331; 
aacpREV[15][ 5] =  396; aacpREV[15][ 6] =  568; aacpREV[15][ 7] =  691; aacpREV[15][ 8] =  303; aacpREV[15][ 9] =  216; 
aacpREV[15][10] =  516; aacpREV[15][11] =  868; aacpREV[15][12] =   93; aacpREV[15][13] =  487; aacpREV[15][14] = 1202; 
aacpREV[15][15] =    0; aacpREV[15][16] = 2151; aacpREV[15][17] =   73; aacpREV[15][18] =  522; aacpREV[15][19] =  167; 
aacpREV[16][ 0] = 1340; aacpREV[16][ 1] =  314; aacpREV[16][ 2] = 1393; aacpREV[16][ 3] =  266; aacpREV[16][ 4] =  576; 
aacpREV[16][ 5] =  241; aacpREV[16][ 6] =  369; aacpREV[16][ 7] =   92; aacpREV[16][ 8] =   32; aacpREV[16][ 9] = 1040; 
aacpREV[16][10] =  156; aacpREV[16][11] =  918; aacpREV[16][12] =  645; aacpREV[16][13] =  148; aacpREV[16][14] =  260; 
aacpREV[16][15] = 2151; aacpREV[16][16] =    0; aacpREV[16][17] =   29; aacpREV[16][18] =   71; aacpREV[16][19] =  760; 
aacpREV[17][ 0] =   14; aacpREV[17][ 1] =  230; aacpREV[17][ 2] =   40; aacpREV[17][ 3] =   18; aacpREV[17][ 4] =  435; 
aacpREV[17][ 5] =   53; aacpREV[17][ 6] =   63; aacpREV[17][ 7] =   82; aacpREV[17][ 8] =   69; aacpREV[17][ 9] =   42; 
aacpREV[17][10] =  159; aacpREV[17][11] =   10; aacpREV[17][12] =   86; aacpREV[17][13] =  468; aacpREV[17][14] =   49; 
aacpREV[17][15] =   73; aacpREV[17][16] =   29; aacpREV[17][17] =    0; aacpREV[17][18] =  346; aacpREV[17][19] =   10; 
aacpREV[18][ 0] =   56; aacpREV[18][ 1] =  323; aacpREV[18][ 2] =  754; aacpREV[18][ 3] =  281; aacpREV[18][ 4] = 1466; 
aacpREV[18][ 5] =  391; aacpREV[18][ 6] =  142; aacpREV[18][ 7] =   10; aacpREV[18][ 8] = 1971; aacpREV[18][ 9] =   89; 
aacpREV[18][10] =  189; aacpREV[18][11] =  247; aacpREV[18][12] =  215; aacpREV[18][13] = 2370; aacpREV[18][14] =   97; 
aacpREV[18][15] =  522; aacpREV[18][16] =   71; aacpREV[18][17] =  346; aacpREV[18][18] =    0; aacpREV[18][19] =  119; 
aacpREV[19][ 0] =  968; aacpREV[19][ 1] =   92; aacpREV[19][ 2] =   83; aacpREV[19][ 3] =   75; aacpREV[19][ 4] =  592; 
aacpREV[19][ 5] =   54; aacpREV[19][ 6] =  200; aacpREV[19][ 7] =   91; aacpREV[19][ 8] =   25; aacpREV[19][ 9] = 4797; 
aacpREV[19][10] =  865; aacpREV[19][11] =  249; aacpREV[19][12] =  475; aacpREV[19][13] =  317; aacpREV[19][14] =  122; 
aacpREV[19][15] =  167; aacpREV[19][16] =  760; aacpREV[19][17] =   10; aacpREV[19][18] =  119; aacpREV[19][19] =    0; 

cprevPi=20*[0]
cprevPi[0] = 0.076;
cprevPi[1] = 0.062;
cprevPi[2] = 0.041;
cprevPi[3] = 0.037;
cprevPi[4] = 0.009;
cprevPi[5] = 0.038;
cprevPi[6] = 0.049;
cprevPi[7] = 0.084;
cprevPi[8] = 0.025;
cprevPi[9] = 0.081;
cprevPi[10] = 0.101;
cprevPi[11] = 0.050;
cprevPi[12] = 0.022;
cprevPi[13] = 0.051;
cprevPi[14] = 0.043;
cprevPi[15] = 0.062;
cprevPi[16] = 0.054;
cprevPi[17] = 0.018;
cprevPi[18] = 0.031;
cprevPi[19] = 0.066;

out=""
for i in range(20):
    for j in range(0,i):
        out+=str(aacpREV[i][j])+" "
    out+="\n"

for i in range(20):
    if (i/7==i/7.0):out+="\n"
    out+=str(cprevPi[i])+" "

out+="// this is the end of the file."
handle=open("cprevMrBayes.dat","w")
handle.write(out)
handle.close()

#VT model
aaVt=20*[["0"*20]]
aaVt=[i[0].split("0") for i in aaVt]
aaVt[ 0][ 0] = 0.000000; aaVt[ 0][ 1] = 0.233108; aaVt[ 0][ 2] = 0.199097; aaVt[ 0][ 3] = 0.265145; aaVt[ 0][ 4] = 0.227333; 
aaVt[ 0][ 5] = 0.310084; aaVt[ 0][ 6] = 0.567957; aaVt[ 0][ 7] = 0.876213; aaVt[ 0][ 8] = 0.078692; aaVt[ 0][ 9] = 0.222972; 
aaVt[ 0][10] = 0.424630; aaVt[ 0][11] = 0.393245; aaVt[ 0][12] = 0.211550; aaVt[ 0][13] = 0.116646; aaVt[ 0][14] = 0.399143; 
aaVt[ 0][15] = 1.817198; aaVt[ 0][16] = 0.877877; aaVt[ 0][17] = 0.030309; aaVt[ 0][18] = 0.087061; aaVt[ 0][19] = 1.230985; 
aaVt[ 1][ 0] = 0.233108; aaVt[ 1][ 1] = 0.000000; aaVt[ 1][ 2] = 0.210797; aaVt[ 1][ 3] = 0.105191; aaVt[ 1][ 4] = 0.031726; 
aaVt[ 1][ 5] = 0.493763; aaVt[ 1][ 6] = 0.255240; aaVt[ 1][ 7] = 0.156945; aaVt[ 1][ 8] = 0.213164; aaVt[ 1][ 9] = 0.081510; 
aaVt[ 1][10] = 0.192364; aaVt[ 1][11] = 1.755838; aaVt[ 1][12] = 0.087930; aaVt[ 1][13] = 0.042569; aaVt[ 1][14] = 0.128480; 
aaVt[ 1][15] = 0.292327; aaVt[ 1][16] = 0.204109; aaVt[ 1][17] = 0.046417; aaVt[ 1][18] = 0.097010; aaVt[ 1][19] = 0.113146; 
aaVt[ 2][ 0] = 0.199097; aaVt[ 2][ 1] = 0.210797; aaVt[ 2][ 2] = 0.000000; aaVt[ 2][ 3] = 0.883422; aaVt[ 2][ 4] = 0.027495; 
aaVt[ 2][ 5] = 0.275700; aaVt[ 2][ 6] = 0.270417; aaVt[ 2][ 7] = 0.362028; aaVt[ 2][ 8] = 0.290006; aaVt[ 2][ 9] = 0.087225; 
aaVt[ 2][10] = 0.069245; aaVt[ 2][11] = 0.503060; aaVt[ 2][12] = 0.057420; aaVt[ 2][13] = 0.039769; aaVt[ 2][14] = 0.083956; 
aaVt[ 2][15] = 0.847049; aaVt[ 2][16] = 0.471268; aaVt[ 2][17] = 0.010459; aaVt[ 2][18] = 0.093268; aaVt[ 2][19] = 0.049824; 
aaVt[ 3][ 0] = 0.265145; aaVt[ 3][ 1] = 0.105191; aaVt[ 3][ 2] = 0.883422; aaVt[ 3][ 3] = 0.000000; aaVt[ 3][ 4] = 0.010313; 
aaVt[ 3][ 5] = 0.205842; aaVt[ 3][ 6] = 1.599461; aaVt[ 3][ 7] = 0.311718; aaVt[ 3][ 8] = 0.134252; aaVt[ 3][ 9] = 0.011720; 
aaVt[ 3][10] = 0.060863; aaVt[ 3][11] = 0.261101; aaVt[ 3][12] = 0.012182; aaVt[ 3][13] = 0.016577; aaVt[ 3][14] = 0.160063; 
aaVt[ 3][15] = 0.461519; aaVt[ 3][16] = 0.178197; aaVt[ 3][17] = 0.011393; aaVt[ 3][18] = 0.051664; aaVt[ 3][19] = 0.048769; 
aaVt[ 4][ 0] = 0.227333; aaVt[ 4][ 1] = 0.031726; aaVt[ 4][ 2] = 0.027495; aaVt[ 4][ 3] = 0.010313; aaVt[ 4][ 4] = 0.000000; 
aaVt[ 4][ 5] = 0.004315; aaVt[ 4][ 6] = 0.005321; aaVt[ 4][ 7] = 0.050876; aaVt[ 4][ 8] = 0.016695; aaVt[ 4][ 9] = 0.046398; 
aaVt[ 4][10] = 0.091709; aaVt[ 4][11] = 0.004067; aaVt[ 4][12] = 0.023690; aaVt[ 4][13] = 0.051127; aaVt[ 4][14] = 0.011137; 
aaVt[ 4][15] = 0.175270; aaVt[ 4][16] = 0.079511; aaVt[ 4][17] = 0.007732; aaVt[ 4][18] = 0.042823; aaVt[ 4][19] = 0.163831; 
aaVt[ 5][ 0] = 0.310084; aaVt[ 5][ 1] = 0.493763; aaVt[ 5][ 2] = 0.275700; aaVt[ 5][ 3] = 0.205842; aaVt[ 5][ 4] = 0.004315; 
aaVt[ 5][ 5] = 0.000000; aaVt[ 5][ 6] = 0.960976; aaVt[ 5][ 7] = 0.128660; aaVt[ 5][ 8] = 0.315521; aaVt[ 5][ 9] = 0.054602; 
aaVt[ 5][10] = 0.243530; aaVt[ 5][11] = 0.738208; aaVt[ 5][12] = 0.120801; aaVt[ 5][13] = 0.026235; aaVt[ 5][14] = 0.156570; 
aaVt[ 5][15] = 0.358017; aaVt[ 5][16] = 0.248992; aaVt[ 5][17] = 0.021248; aaVt[ 5][18] = 0.062544; aaVt[ 5][19] = 0.112027; 
aaVt[ 6][ 0] = 0.567957; aaVt[ 6][ 1] = 0.255240; aaVt[ 6][ 2] = 0.270417; aaVt[ 6][ 3] = 1.599461; aaVt[ 6][ 4] = 0.005321; 
aaVt[ 6][ 5] = 0.960976; aaVt[ 6][ 6] = 0.000000; aaVt[ 6][ 7] = 0.250447; aaVt[ 6][ 8] = 0.104458; aaVt[ 6][ 9] = 0.046589; 
aaVt[ 6][10] = 0.151924; aaVt[ 6][11] = 0.888630; aaVt[ 6][12] = 0.058643; aaVt[ 6][13] = 0.028168; aaVt[ 6][14] = 0.205134; 
aaVt[ 6][15] = 0.406035; aaVt[ 6][16] = 0.321028; aaVt[ 6][17] = 0.018844; aaVt[ 6][18] = 0.055200; aaVt[ 6][19] = 0.205868; 
aaVt[ 7][ 0] = 0.876213; aaVt[ 7][ 1] = 0.156945; aaVt[ 7][ 2] = 0.362028; aaVt[ 7][ 3] = 0.311718; aaVt[ 7][ 4] = 0.050876; 
aaVt[ 7][ 5] = 0.128660; aaVt[ 7][ 6] = 0.250447; aaVt[ 7][ 7] = 0.000000; aaVt[ 7][ 8] = 0.058131; aaVt[ 7][ 9] = 0.051089; 
aaVt[ 7][10] = 0.087056; aaVt[ 7][11] = 0.193243; aaVt[ 7][12] = 0.046560; aaVt[ 7][13] = 0.050143; aaVt[ 7][14] = 0.124492; 
aaVt[ 7][15] = 0.612843; aaVt[ 7][16] = 0.136266; aaVt[ 7][17] = 0.023990; aaVt[ 7][18] = 0.037568; aaVt[ 7][19] = 0.082579; 
aaVt[ 8][ 0] = 0.078692; aaVt[ 8][ 1] = 0.213164; aaVt[ 8][ 2] = 0.290006; aaVt[ 8][ 3] = 0.134252; aaVt[ 8][ 4] = 0.016695; 
aaVt[ 8][ 5] = 0.315521; aaVt[ 8][ 6] = 0.104458; aaVt[ 8][ 7] = 0.058131; aaVt[ 8][ 8] = 0.000000; aaVt[ 8][ 9] = 0.020039; 
aaVt[ 8][10] = 0.103552; aaVt[ 8][11] = 0.153323; aaVt[ 8][12] = 0.021157; aaVt[ 8][13] = 0.079807; aaVt[ 8][14] = 0.078892; 
aaVt[ 8][15] = 0.167406; aaVt[ 8][16] = 0.101117; aaVt[ 8][17] = 0.020009; aaVt[ 8][18] = 0.286027; aaVt[ 8][19] = 0.068575; 
aaVt[ 9][ 0] = 0.222972; aaVt[ 9][ 1] = 0.081510; aaVt[ 9][ 2] = 0.087225; aaVt[ 9][ 3] = 0.011720; aaVt[ 9][ 4] = 0.046398; 
aaVt[ 9][ 5] = 0.054602; aaVt[ 9][ 6] = 0.046589; aaVt[ 9][ 7] = 0.051089; aaVt[ 9][ 8] = 0.020039; aaVt[ 9][ 9] = 0.000000; 
aaVt[ 9][10] = 2.089890; aaVt[ 9][11] = 0.093181; aaVt[ 9][12] = 0.493845; aaVt[ 9][13] = 0.321020; aaVt[ 9][14] = 0.054797; 
aaVt[ 9][15] = 0.081567; aaVt[ 9][16] = 0.376588; aaVt[ 9][17] = 0.034954; aaVt[ 9][18] = 0.086237; aaVt[ 9][19] = 3.654430; 
aaVt[10][ 0] = 0.424630; aaVt[10][ 1] = 0.192364; aaVt[10][ 2] = 0.069245; aaVt[10][ 3] = 0.060863; aaVt[10][ 4] = 0.091709; 
aaVt[10][ 5] = 0.243530; aaVt[10][ 6] = 0.151924; aaVt[10][ 7] = 0.087056; aaVt[10][ 8] = 0.103552; aaVt[10][ 9] = 2.089890; 
aaVt[10][10] = 0.000000; aaVt[10][11] = 0.201204; aaVt[10][12] = 1.105667; aaVt[10][13] = 0.946499; aaVt[10][14] = 0.169784; 
aaVt[10][15] = 0.214977; aaVt[10][16] = 0.243227; aaVt[10][17] = 0.083439; aaVt[10][18] = 0.189842; aaVt[10][19] = 1.337571; 
aaVt[11][ 0] = 0.393245; aaVt[11][ 1] = 1.755838; aaVt[11][ 2] = 0.503060; aaVt[11][ 3] = 0.261101; aaVt[11][ 4] = 0.004067; 
aaVt[11][ 5] = 0.738208; aaVt[11][ 6] = 0.888630; aaVt[11][ 7] = 0.193243; aaVt[11][ 8] = 0.153323; aaVt[11][ 9] = 0.093181; 
aaVt[11][10] = 0.201204; aaVt[11][11] = 0.000000; aaVt[11][12] = 0.096474; aaVt[11][13] = 0.038261; aaVt[11][14] = 0.212302; 
aaVt[11][15] = 0.400072; aaVt[11][16] = 0.446646; aaVt[11][17] = 0.023321; aaVt[11][18] = 0.068689; aaVt[11][19] = 0.144587; 
aaVt[12][ 0] = 0.211550; aaVt[12][ 1] = 0.087930; aaVt[12][ 2] = 0.057420; aaVt[12][ 3] = 0.012182; aaVt[12][ 4] = 0.023690; 
aaVt[12][ 5] = 0.120801; aaVt[12][ 6] = 0.058643; aaVt[12][ 7] = 0.046560; aaVt[12][ 8] = 0.021157; aaVt[12][ 9] = 0.493845; 
aaVt[12][10] = 1.105667; aaVt[12][11] = 0.096474; aaVt[12][12] = 0.000000; aaVt[12][13] = 0.173052; aaVt[12][14] = 0.010363; 
aaVt[12][15] = 0.090515; aaVt[12][16] = 0.184609; aaVt[12][17] = 0.022019; aaVt[12][18] = 0.073223; aaVt[12][19] = 0.307309; 
aaVt[13][ 0] = 0.116646; aaVt[13][ 1] = 0.042569; aaVt[13][ 2] = 0.039769; aaVt[13][ 3] = 0.016577; aaVt[13][ 4] = 0.051127; 
aaVt[13][ 5] = 0.026235; aaVt[13][ 6] = 0.028168; aaVt[13][ 7] = 0.050143; aaVt[13][ 8] = 0.079807; aaVt[13][ 9] = 0.321020; 
aaVt[13][10] = 0.946499; aaVt[13][11] = 0.038261; aaVt[13][12] = 0.173052; aaVt[13][13] = 0.000000; aaVt[13][14] = 0.042564; 
aaVt[13][15] = 0.138119; aaVt[13][16] = 0.085870; aaVt[13][17] = 0.128050; aaVt[13][18] = 0.898663; aaVt[13][19] = 0.247329; 
aaVt[14][ 0] = 0.399143; aaVt[14][ 1] = 0.128480; aaVt[14][ 2] = 0.083956; aaVt[14][ 3] = 0.160063; aaVt[14][ 4] = 0.011137; 
aaVt[14][ 5] = 0.156570; aaVt[14][ 6] = 0.205134; aaVt[14][ 7] = 0.124492; aaVt[14][ 8] = 0.078892; aaVt[14][ 9] = 0.054797; 
aaVt[14][10] = 0.169784; aaVt[14][11] = 0.212302; aaVt[14][12] = 0.010363; aaVt[14][13] = 0.042564; aaVt[14][14] = 0.000000; 
aaVt[14][15] = 0.430431; aaVt[14][16] = 0.207143; aaVt[14][17] = 0.014584; aaVt[14][18] = 0.032043; aaVt[14][19] = 0.129315; 
aaVt[15][ 0] = 1.817198; aaVt[15][ 1] = 0.292327; aaVt[15][ 2] = 0.847049; aaVt[15][ 3] = 0.461519; aaVt[15][ 4] = 0.175270; 
aaVt[15][ 5] = 0.358017; aaVt[15][ 6] = 0.406035; aaVt[15][ 7] = 0.612843; aaVt[15][ 8] = 0.167406; aaVt[15][ 9] = 0.081567; 
aaVt[15][10] = 0.214977; aaVt[15][11] = 0.400072; aaVt[15][12] = 0.090515; aaVt[15][13] = 0.138119; aaVt[15][14] = 0.430431; 
aaVt[15][15] = 0.000000; aaVt[15][16] = 1.767766; aaVt[15][17] = 0.035933; aaVt[15][18] = 0.121979; aaVt[15][19] = 0.127700; 
aaVt[16][ 0] = 0.877877; aaVt[16][ 1] = 0.204109; aaVt[16][ 2] = 0.471268; aaVt[16][ 3] = 0.178197; aaVt[16][ 4] = 0.079511; 
aaVt[16][ 5] = 0.248992; aaVt[16][ 6] = 0.321028; aaVt[16][ 7] = 0.136266; aaVt[16][ 8] = 0.101117; aaVt[16][ 9] = 0.376588; 
aaVt[16][10] = 0.243227; aaVt[16][11] = 0.446646; aaVt[16][12] = 0.184609; aaVt[16][13] = 0.085870; aaVt[16][14] = 0.207143; 
aaVt[16][15] = 1.767766; aaVt[16][16] = 0.000000; aaVt[16][17] = 0.020437; aaVt[16][18] = 0.094617; aaVt[16][19] = 0.740372; 
aaVt[17][ 0] = 0.030309; aaVt[17][ 1] = 0.046417; aaVt[17][ 2] = 0.010459; aaVt[17][ 3] = 0.011393; aaVt[17][ 4] = 0.007732; 
aaVt[17][ 5] = 0.021248; aaVt[17][ 6] = 0.018844; aaVt[17][ 7] = 0.023990; aaVt[17][ 8] = 0.020009; aaVt[17][ 9] = 0.034954; 
aaVt[17][10] = 0.083439; aaVt[17][11] = 0.023321; aaVt[17][12] = 0.022019; aaVt[17][13] = 0.128050; aaVt[17][14] = 0.014584; 
aaVt[17][15] = 0.035933; aaVt[17][16] = 0.020437; aaVt[17][17] = 0.000000; aaVt[17][18] = 0.124746; aaVt[17][19] = 0.022134; 
aaVt[18][ 0] = 0.087061; aaVt[18][ 1] = 0.097010; aaVt[18][ 2] = 0.093268; aaVt[18][ 3] = 0.051664; aaVt[18][ 4] = 0.042823; 
aaVt[18][ 5] = 0.062544; aaVt[18][ 6] = 0.055200; aaVt[18][ 7] = 0.037568; aaVt[18][ 8] = 0.286027; aaVt[18][ 9] = 0.086237; 
aaVt[18][10] = 0.189842; aaVt[18][11] = 0.068689; aaVt[18][12] = 0.073223; aaVt[18][13] = 0.898663; aaVt[18][14] = 0.032043; 
aaVt[18][15] = 0.121979; aaVt[18][16] = 0.094617; aaVt[18][17] = 0.124746; aaVt[18][18] = 0.000000; aaVt[18][19] = 0.125733; 
aaVt[19][ 0] = 1.230985; aaVt[19][ 1] = 0.113146; aaVt[19][ 2] = 0.049824; aaVt[19][ 3] = 0.048769; aaVt[19][ 4] = 0.163831; 
aaVt[19][ 5] = 0.112027; aaVt[19][ 6] = 0.205868; aaVt[19][ 7] = 0.082579; aaVt[19][ 8] = 0.068575; aaVt[19][ 9] = 3.654430; 
aaVt[19][10] = 1.337571; aaVt[19][11] = 0.144587; aaVt[19][12] = 0.307309; aaVt[19][13] = 0.247329; aaVt[19][14] = 0.129315; 
aaVt[19][15] = 0.127700; aaVt[19][16] = 0.740372; aaVt[19][17] = 0.022134; aaVt[19][18] = 0.125733; aaVt[19][19] = 0.000000; 

vtPi=20*[0]
vtPi[ 0] = 0.078837;
vtPi[ 1] = 0.051238;
vtPi[ 2] = 0.042313;
vtPi[ 3] = 0.053066;
vtPi[ 4] = 0.015175;
vtPi[ 5] = 0.036713;
vtPi[ 6] = 0.061924;
vtPi[ 7] = 0.070852;
vtPi[ 8] = 0.023082;
vtPi[ 9] = 0.062056;
vtPi[10] = 0.096371;
vtPi[11] = 0.057324;
vtPi[12] = 0.023771;
vtPi[13] = 0.043296;
vtPi[14] = 0.043911;
vtPi[15] = 0.063403;
vtPi[16] = 0.055897;
vtPi[17] = 0.013272;
vtPi[18] = 0.034399;
vtPi[19] = 0.073101;

out=""
for i in range(20):
    for j in range(0,i):
        out+=str(aaVt[i][j])+" "
    out+="\n"

for i in range(20):
    if (i/7==i/7.0):out+="\n"
    out+=str(vtPi[i])+" "

out+="// this is the end of the file."
handle=open("vtMrBayes.dat","w")
handle.write(out)
handle.close()

#Blosum62 */
aaBlosum=20*[["0"*20]]
aaBlosum=[i[0].split("0") for i in aaBlosum]
aaBlosum[ 0][ 0] = 0.000000000000; aaBlosum[ 0][ 1] = 0.735790389698; aaBlosum[ 0][ 2] = 0.485391055466; aaBlosum[ 0][ 3] = 0.543161820899; aaBlosum[ 0][ 4] = 1.459995310470; 
aaBlosum[ 0][ 5] = 1.199705704602; aaBlosum[ 0][ 6] = 1.170949042800; aaBlosum[ 0][ 7] = 1.955883574960; aaBlosum[ 0][ 8] = 0.716241444998; aaBlosum[ 0][ 9] = 0.605899003687; 
aaBlosum[ 0][10] = 0.800016530518; aaBlosum[ 0][11] = 1.295201266783; aaBlosum[ 0][12] = 1.253758266664; aaBlosum[ 0][13] = 0.492964679748; aaBlosum[ 0][14] = 1.173275900924; 
aaBlosum[ 0][15] = 4.325092687057; aaBlosum[ 0][16] = 1.729178019485; aaBlosum[ 0][17] = 0.465839367725; aaBlosum[ 0][18] = 0.718206697586; aaBlosum[ 0][19] = 2.187774522005; 
aaBlosum[ 1][ 0] = 0.735790389698; aaBlosum[ 1][ 1] = 0.000000000000; aaBlosum[ 1][ 2] = 1.297446705134; aaBlosum[ 1][ 3] = 0.500964408555; aaBlosum[ 1][ 4] = 0.227826574209; 
aaBlosum[ 1][ 5] = 3.020833610064; aaBlosum[ 1][ 6] = 1.360574190420; aaBlosum[ 1][ 7] = 0.418763308518; aaBlosum[ 1][ 8] = 1.456141166336; aaBlosum[ 1][ 9] = 0.232036445142; 
aaBlosum[ 1][10] = 0.622711669692; aaBlosum[ 1][11] = 5.411115141489; aaBlosum[ 1][12] = 0.983692987457; aaBlosum[ 1][13] = 0.371644693209; aaBlosum[ 1][14] = 0.448133661718; 
aaBlosum[ 1][15] = 1.122783104210; aaBlosum[ 1][16] = 0.914665954563; aaBlosum[ 1][17] = 0.426382310122; aaBlosum[ 1][18] = 0.720517441216; aaBlosum[ 1][19] = 0.438388343772; 
aaBlosum[ 2][ 0] = 0.485391055466; aaBlosum[ 2][ 1] = 1.297446705134; aaBlosum[ 2][ 2] = 0.000000000000; aaBlosum[ 2][ 3] = 3.180100048216; aaBlosum[ 2][ 4] = 0.397358949897; 
aaBlosum[ 2][ 5] = 1.839216146992; aaBlosum[ 2][ 6] = 1.240488508640; aaBlosum[ 2][ 7] = 1.355872344485; aaBlosum[ 2][ 8] = 2.414501434208; aaBlosum[ 2][ 9] = 0.283017326278; 
aaBlosum[ 2][10] = 0.211888159615; aaBlosum[ 2][11] = 1.593137043457; aaBlosum[ 2][12] = 0.648441278787; aaBlosum[ 2][13] = 0.354861249223; aaBlosum[ 2][14] = 0.494887043702; 
aaBlosum[ 2][15] = 2.904101656456; aaBlosum[ 2][16] = 1.898173634533; aaBlosum[ 2][17] = 0.191482046247; aaBlosum[ 2][18] = 0.538222519037; aaBlosum[ 2][19] = 0.312858797993; 
aaBlosum[ 3][ 0] = 0.543161820899; aaBlosum[ 3][ 1] = 0.500964408555; aaBlosum[ 3][ 2] = 3.180100048216; aaBlosum[ 3][ 3] = 0.000000000000; aaBlosum[ 3][ 4] = 0.240836614802; 
aaBlosum[ 3][ 5] = 1.190945703396; aaBlosum[ 3][ 6] = 3.761625208368; aaBlosum[ 3][ 7] = 0.798473248968; aaBlosum[ 3][ 8] = 0.778142664022; aaBlosum[ 3][ 9] = 0.418555732462; 
aaBlosum[ 3][10] = 0.218131577594; aaBlosum[ 3][11] = 1.032447924952; aaBlosum[ 3][12] = 0.222621897958; aaBlosum[ 3][13] = 0.281730694207; aaBlosum[ 3][14] = 0.730628272998; 
aaBlosum[ 3][15] = 1.582754142065; aaBlosum[ 3][16] = 0.934187509431; aaBlosum[ 3][17] = 0.145345046279; aaBlosum[ 3][18] = 0.261422208965; aaBlosum[ 3][19] = 0.258129289418; 
aaBlosum[ 4][ 0] = 1.459995310470; aaBlosum[ 4][ 1] = 0.227826574209; aaBlosum[ 4][ 2] = 0.397358949897; aaBlosum[ 4][ 3] = 0.240836614802; aaBlosum[ 4][ 4] = 0.000000000000; 
aaBlosum[ 4][ 5] = 0.329801504630; aaBlosum[ 4][ 6] = 0.140748891814; aaBlosum[ 4][ 7] = 0.418203192284; aaBlosum[ 4][ 8] = 0.354058109831; aaBlosum[ 4][ 9] = 0.774894022794; 
aaBlosum[ 4][10] = 0.831842640142; aaBlosum[ 4][11] = 0.285078800906; aaBlosum[ 4][12] = 0.767688823480; aaBlosum[ 4][13] = 0.441337471187; aaBlosum[ 4][14] = 0.356008498769; 
aaBlosum[ 4][15] = 1.197188415094; aaBlosum[ 4][16] = 1.119831358516; aaBlosum[ 4][17] = 0.527664418872; aaBlosum[ 4][18] = 0.470237733696; aaBlosum[ 4][19] = 1.116352478606; 
aaBlosum[ 5][ 0] = 1.199705704602; aaBlosum[ 5][ 1] = 3.020833610064; aaBlosum[ 5][ 2] = 1.839216146992; aaBlosum[ 5][ 3] = 1.190945703396; aaBlosum[ 5][ 4] = 0.329801504630; 
aaBlosum[ 5][ 5] = 0.000000000000; aaBlosum[ 5][ 6] = 5.528919177928; aaBlosum[ 5][ 7] = 0.609846305383; aaBlosum[ 5][ 8] = 2.435341131140; aaBlosum[ 5][ 9] = 0.236202451204; 
aaBlosum[ 5][10] = 0.580737093181; aaBlosum[ 5][11] = 3.945277674515; aaBlosum[ 5][12] = 2.494896077113; aaBlosum[ 5][13] = 0.144356959750; aaBlosum[ 5][14] = 0.858570575674; 
aaBlosum[ 5][15] = 1.934870924596; aaBlosum[ 5][16] = 1.277480294596; aaBlosum[ 5][17] = 0.758653808642; aaBlosum[ 5][18] = 0.958989742850; aaBlosum[ 5][19] = 0.530785790125; 
aaBlosum[ 6][ 0] = 1.170949042800; aaBlosum[ 6][ 1] = 1.360574190420; aaBlosum[ 6][ 2] = 1.240488508640; aaBlosum[ 6][ 3] = 3.761625208368; aaBlosum[ 6][ 4] = 0.140748891814; 
aaBlosum[ 6][ 5] = 5.528919177928; aaBlosum[ 6][ 6] = 0.000000000000; aaBlosum[ 6][ 7] = 0.423579992176; aaBlosum[ 6][ 8] = 1.626891056982; aaBlosum[ 6][ 9] = 0.186848046932; 
aaBlosum[ 6][10] = 0.372625175087; aaBlosum[ 6][11] = 2.802427151679; aaBlosum[ 6][12] = 0.555415397470; aaBlosum[ 6][13] = 0.291409084165; aaBlosum[ 6][14] = 0.926563934846; 
aaBlosum[ 6][15] = 1.769893238937; aaBlosum[ 6][16] = 1.071097236007; aaBlosum[ 6][17] = 0.407635648938; aaBlosum[ 6][18] = 0.596719300346; aaBlosum[ 6][19] = 0.524253846338; 
aaBlosum[ 7][ 0] = 1.955883574960; aaBlosum[ 7][ 1] = 0.418763308518; aaBlosum[ 7][ 2] = 1.355872344485; aaBlosum[ 7][ 3] = 0.798473248968; aaBlosum[ 7][ 4] = 0.418203192284; 
aaBlosum[ 7][ 5] = 0.609846305383; aaBlosum[ 7][ 6] = 0.423579992176; aaBlosum[ 7][ 7] = 0.000000000000; aaBlosum[ 7][ 8] = 0.539859124954; aaBlosum[ 7][ 9] = 0.189296292376; 
aaBlosum[ 7][10] = 0.217721159236; aaBlosum[ 7][11] = 0.752042440303; aaBlosum[ 7][12] = 0.459436173579; aaBlosum[ 7][13] = 0.368166464453; aaBlosum[ 7][14] = 0.504086599527; 
aaBlosum[ 7][15] = 1.509326253224; aaBlosum[ 7][16] = 0.641436011405; aaBlosum[ 7][17] = 0.508358924638; aaBlosum[ 7][18] = 0.308055737035; aaBlosum[ 7][19] = 0.253340790190; 
aaBlosum[ 8][ 0] = 0.716241444998; aaBlosum[ 8][ 1] = 1.456141166336; aaBlosum[ 8][ 2] = 2.414501434208; aaBlosum[ 8][ 3] = 0.778142664022; aaBlosum[ 8][ 4] = 0.354058109831; 
aaBlosum[ 8][ 5] = 2.435341131140; aaBlosum[ 8][ 6] = 1.626891056982; aaBlosum[ 8][ 7] = 0.539859124954; aaBlosum[ 8][ 8] = 0.000000000000; aaBlosum[ 8][ 9] = 0.252718447885; 
aaBlosum[ 8][10] = 0.348072209797; aaBlosum[ 8][11] = 1.022507035889; aaBlosum[ 8][12] = 0.984311525359; aaBlosum[ 8][13] = 0.714533703928; aaBlosum[ 8][14] = 0.527007339151; 
aaBlosum[ 8][15] = 1.117029762910; aaBlosum[ 8][16] = 0.585407090225; aaBlosum[ 8][17] = 0.301248600780; aaBlosum[ 8][18] = 4.218953969389; aaBlosum[ 8][19] = 0.201555971750; 
aaBlosum[ 9][ 0] = 0.605899003687; aaBlosum[ 9][ 1] = 0.232036445142; aaBlosum[ 9][ 2] = 0.283017326278; aaBlosum[ 9][ 3] = 0.418555732462; aaBlosum[ 9][ 4] = 0.774894022794; 
aaBlosum[ 9][ 5] = 0.236202451204; aaBlosum[ 9][ 6] = 0.186848046932; aaBlosum[ 9][ 7] = 0.189296292376; aaBlosum[ 9][ 8] = 0.252718447885; aaBlosum[ 9][ 9] = 0.000000000000; 
aaBlosum[ 9][10] = 3.890963773304; aaBlosum[ 9][11] = 0.406193586642; aaBlosum[ 9][12] = 3.364797763104; aaBlosum[ 9][13] = 1.517359325954; aaBlosum[ 9][14] = 0.388355409206; 
aaBlosum[ 9][15] = 0.357544412460; aaBlosum[ 9][16] = 1.179091197260; aaBlosum[ 9][17] = 0.341985787540; aaBlosum[ 9][18] = 0.674617093228; aaBlosum[ 9][19] = 8.311839405458; 
aaBlosum[10][ 0] = 0.800016530518; aaBlosum[10][ 1] = 0.622711669692; aaBlosum[10][ 2] = 0.211888159615; aaBlosum[10][ 3] = 0.218131577594; aaBlosum[10][ 4] = 0.831842640142; 
aaBlosum[10][ 5] = 0.580737093181; aaBlosum[10][ 6] = 0.372625175087; aaBlosum[10][ 7] = 0.217721159236; aaBlosum[10][ 8] = 0.348072209797; aaBlosum[10][ 9] = 3.890963773304; 
aaBlosum[10][10] = 0.000000000000; aaBlosum[10][11] = 0.445570274261; aaBlosum[10][12] = 6.030559379572; aaBlosum[10][13] = 2.064839703237; aaBlosum[10][14] = 0.374555687471; 
aaBlosum[10][15] = 0.352969184527; aaBlosum[10][16] = 0.915259857694; aaBlosum[10][17] = 0.691474634600; aaBlosum[10][18] = 0.811245856323; aaBlosum[10][19] = 2.231405688913; 
aaBlosum[11][ 0] = 1.295201266783; aaBlosum[11][ 1] = 5.411115141489; aaBlosum[11][ 2] = 1.593137043457; aaBlosum[11][ 3] = 1.032447924952; aaBlosum[11][ 4] = 0.285078800906; 
aaBlosum[11][ 5] = 3.945277674515; aaBlosum[11][ 6] = 2.802427151679; aaBlosum[11][ 7] = 0.752042440303; aaBlosum[11][ 8] = 1.022507035889; aaBlosum[11][ 9] = 0.406193586642; 
aaBlosum[11][10] = 0.445570274261; aaBlosum[11][11] = 0.000000000000; aaBlosum[11][12] = 1.073061184332; aaBlosum[11][13] = 0.266924750511; aaBlosum[11][14] = 1.047383450722; 
aaBlosum[11][15] = 1.752165917819; aaBlosum[11][16] = 1.303875200799; aaBlosum[11][17] = 0.332243040634; aaBlosum[11][18] = 0.717993486900; aaBlosum[11][19] = 0.498138475304; 
aaBlosum[12][ 0] = 1.253758266664; aaBlosum[12][ 1] = 0.983692987457; aaBlosum[12][ 2] = 0.648441278787; aaBlosum[12][ 3] = 0.222621897958; aaBlosum[12][ 4] = 0.767688823480; 
aaBlosum[12][ 5] = 2.494896077113; aaBlosum[12][ 6] = 0.555415397470; aaBlosum[12][ 7] = 0.459436173579; aaBlosum[12][ 8] = 0.984311525359; aaBlosum[12][ 9] = 3.364797763104; 
aaBlosum[12][10] = 6.030559379572; aaBlosum[12][11] = 1.073061184332; aaBlosum[12][12] = 0.000000000000; aaBlosum[12][13] = 1.773855168830; aaBlosum[12][14] = 0.454123625103; 
aaBlosum[12][15] = 0.918723415746; aaBlosum[12][16] = 1.488548053722; aaBlosum[12][17] = 0.888101098152; aaBlosum[12][18] = 0.951682162246; aaBlosum[12][19] = 2.575850755315; 
aaBlosum[13][ 0] = 0.492964679748; aaBlosum[13][ 1] = 0.371644693209; aaBlosum[13][ 2] = 0.354861249223; aaBlosum[13][ 3] = 0.281730694207; aaBlosum[13][ 4] = 0.441337471187; 
aaBlosum[13][ 5] = 0.144356959750; aaBlosum[13][ 6] = 0.291409084165; aaBlosum[13][ 7] = 0.368166464453; aaBlosum[13][ 8] = 0.714533703928; aaBlosum[13][ 9] = 1.517359325954; 
aaBlosum[13][10] = 2.064839703237; aaBlosum[13][11] = 0.266924750511; aaBlosum[13][12] = 1.773855168830; aaBlosum[13][13] = 0.000000000000; aaBlosum[13][14] = 0.233597909629; 
aaBlosum[13][15] = 0.540027644824; aaBlosum[13][16] = 0.488206118793; aaBlosum[13][17] = 2.074324893497; aaBlosum[13][18] = 6.747260430801; aaBlosum[13][19] = 0.838119610178; 
aaBlosum[14][ 0] = 1.173275900924; aaBlosum[14][ 1] = 0.448133661718; aaBlosum[14][ 2] = 0.494887043702; aaBlosum[14][ 3] = 0.730628272998; aaBlosum[14][ 4] = 0.356008498769; 
aaBlosum[14][ 5] = 0.858570575674; aaBlosum[14][ 6] = 0.926563934846; aaBlosum[14][ 7] = 0.504086599527; aaBlosum[14][ 8] = 0.527007339151; aaBlosum[14][ 9] = 0.388355409206; 
aaBlosum[14][10] = 0.374555687471; aaBlosum[14][11] = 1.047383450722; aaBlosum[14][12] = 0.454123625103; aaBlosum[14][13] = 0.233597909629; aaBlosum[14][14] = 0.000000000000; 
aaBlosum[14][15] = 1.169129577716; aaBlosum[14][16] = 1.005451683149; aaBlosum[14][17] = 0.252214830027; aaBlosum[14][18] = 0.369405319355; aaBlosum[14][19] = 0.496908410676; 
aaBlosum[15][ 0] = 4.325092687057; aaBlosum[15][ 1] = 1.122783104210; aaBlosum[15][ 2] = 2.904101656456; aaBlosum[15][ 3] = 1.582754142065; aaBlosum[15][ 4] = 1.197188415094; 
aaBlosum[15][ 5] = 1.934870924596; aaBlosum[15][ 6] = 1.769893238937; aaBlosum[15][ 7] = 1.509326253224; aaBlosum[15][ 8] = 1.117029762910; aaBlosum[15][ 9] = 0.357544412460; 
aaBlosum[15][10] = 0.352969184527; aaBlosum[15][11] = 1.752165917819; aaBlosum[15][12] = 0.918723415746; aaBlosum[15][13] = 0.540027644824; aaBlosum[15][14] = 1.169129577716; 
aaBlosum[15][15] = 0.000000000000; aaBlosum[15][16] = 5.151556292270; aaBlosum[15][17] = 0.387925622098; aaBlosum[15][18] = 0.796751520761; aaBlosum[15][19] = 0.561925457442; 
aaBlosum[16][ 0] = 1.729178019485; aaBlosum[16][ 1] = 0.914665954563; aaBlosum[16][ 2] = 1.898173634533; aaBlosum[16][ 3] = 0.934187509431; aaBlosum[16][ 4] = 1.119831358516; 
aaBlosum[16][ 5] = 1.277480294596; aaBlosum[16][ 6] = 1.071097236007; aaBlosum[16][ 7] = 0.641436011405; aaBlosum[16][ 8] = 0.585407090225; aaBlosum[16][ 9] = 1.179091197260; 
aaBlosum[16][10] = 0.915259857694; aaBlosum[16][11] = 1.303875200799; aaBlosum[16][12] = 1.488548053722; aaBlosum[16][13] = 0.488206118793; aaBlosum[16][14] = 1.005451683149; 
aaBlosum[16][15] = 5.151556292270; aaBlosum[16][16] = 0.000000000000; aaBlosum[16][17] = 0.513128126891; aaBlosum[16][18] = 0.801010243199; aaBlosum[16][19] = 2.253074051176; 
aaBlosum[17][ 0] = 0.465839367725; aaBlosum[17][ 1] = 0.426382310122; aaBlosum[17][ 2] = 0.191482046247; aaBlosum[17][ 3] = 0.145345046279; aaBlosum[17][ 4] = 0.527664418872; 
aaBlosum[17][ 5] = 0.758653808642; aaBlosum[17][ 6] = 0.407635648938; aaBlosum[17][ 7] = 0.508358924638; aaBlosum[17][ 8] = 0.301248600780; aaBlosum[17][ 9] = 0.341985787540; 
aaBlosum[17][10] = 0.691474634600; aaBlosum[17][11] = 0.332243040634; aaBlosum[17][12] = 0.888101098152; aaBlosum[17][13] = 2.074324893497; aaBlosum[17][14] = 0.252214830027; 
aaBlosum[17][15] = 0.387925622098; aaBlosum[17][16] = 0.513128126891; aaBlosum[17][17] = 0.000000000000; aaBlosum[17][18] = 4.054419006558; aaBlosum[17][19] = 0.266508731426; 
aaBlosum[18][ 0] = 0.718206697586; aaBlosum[18][ 1] = 0.720517441216; aaBlosum[18][ 2] = 0.538222519037; aaBlosum[18][ 3] = 0.261422208965; aaBlosum[18][ 4] = 0.470237733696; 
aaBlosum[18][ 5] = 0.958989742850; aaBlosum[18][ 6] = 0.596719300346; aaBlosum[18][ 7] = 0.308055737035; aaBlosum[18][ 8] = 4.218953969389; aaBlosum[18][ 9] = 0.674617093228; 
aaBlosum[18][10] = 0.811245856323; aaBlosum[18][11] = 0.717993486900; aaBlosum[18][12] = 0.951682162246; aaBlosum[18][13] = 6.747260430801; aaBlosum[18][14] = 0.369405319355; 
aaBlosum[18][15] = 0.796751520761; aaBlosum[18][16] = 0.801010243199; aaBlosum[18][17] = 4.054419006558; aaBlosum[18][18] = 0.000000000000; aaBlosum[18][19] = 1.000000000000; 
aaBlosum[19][ 0] = 2.187774522005; aaBlosum[19][ 1] = 0.438388343772; aaBlosum[19][ 2] = 0.312858797993; aaBlosum[19][ 3] = 0.258129289418; aaBlosum[19][ 4] = 1.116352478606; 
aaBlosum[19][ 5] = 0.530785790125; aaBlosum[19][ 6] = 0.524253846338; aaBlosum[19][ 7] = 0.253340790190; aaBlosum[19][ 8] = 0.201555971750; aaBlosum[19][ 9] = 8.311839405458; 
aaBlosum[19][10] = 2.231405688913; aaBlosum[19][11] = 0.498138475304; aaBlosum[19][12] = 2.575850755315; aaBlosum[19][13] = 0.838119610178; aaBlosum[19][14] = 0.496908410676; 
aaBlosum[19][15] = 0.561925457442; aaBlosum[19][16] = 2.253074051176; aaBlosum[19][17] = 0.266508731426; aaBlosum[19][18] = 1.000000000000; aaBlosum[19][19] = 0.000000000000; 	

blosPi=20*[0]
blosPi[ 0] = 0.074; 
blosPi[ 1] = 0.052; 
blosPi[ 2] = 0.045; 
blosPi[ 3] = 0.054;
blosPi[ 4] = 0.025; 
blosPi[ 5] = 0.034; 
blosPi[ 6] = 0.054; 
blosPi[ 7] = 0.074;
blosPi[ 8] = 0.026; 
blosPi[ 9] = 0.068; 
blosPi[10] = 0.099; 
blosPi[11] = 0.058;
blosPi[12] = 0.025; 
blosPi[13] = 0.047; 
blosPi[14] = 0.039; 
blosPi[15] = 0.057;
blosPi[16] = 0.051; 
blosPi[17] = 0.013; 
blosPi[18] = 0.032; 
blosPi[19] = 0.073;

out=""
for i in range(20):
    for j in range(0,i):
        out+=str(aaBlosum[i][j])+" "
    out+="\n"

for i in range(20):
    if (i/7==i/7.0):out+="\n"
    out+=str(blosPi[i])+" "

out+="// this is the end of the file."
handle=open("blosumMrBayes.dat","w")
handle.write(out)
handle.close()

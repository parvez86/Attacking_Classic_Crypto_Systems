def get_plaintext(text, number):
    # each index represents the nth alphabetic characters of input text
    # each index value represents the corresponding decipher or plaintext text

    # for 1st text
    keystream1 = ['', 'Y', 'W', 'L', 'C', 'N', 'O', 'P', 'H', 'S', 'R', '', 'T', 'A', 'I', 'J', 'K', 'B',
                  'M', 'E', 'G', '', 'U', 'V', 'F', 'D']

    # for 2nd text
    keystream2 = ['V', 'U', 'S', 'H', 'A', 'L', 'M', 'N', 'F', 'Q', 'P', 'O', 'R', 'W', 'G', 'Y', 'Z', 'X', 'I', 'C',
                  'E', 'T', 'J', 'K', 'D', 'B']

    keystream = list()
    if number == 1:
        keystream = keystream1.copy()
    else:
        keystream = keystream2.copy()

    length = len(text)
    result = ''
    for char in text:
        if str.isalpha(char):
            result += keystream[ord(char)-ord('A')]
        else:
            result += char

    return result


def decipher(text, number):
    # frequency distribution table
    freq_dist_table = {
        'A': 8.05, 'B': 1.67, 'C': 2.23, 'D': 5.10, 'E': 12.22,
        'F': 2.14, 'G': 2.30, 'H': 6.62, 'I': 6.28, 'J': 0.19,
        'K': 0.95, 'L': 4.08, 'M': 2.33, 'N': 6.95, 'O': 7.63,
        'P': 1.66, 'Q': 0.061, 'R': 5.29, 'S': 6.02, 'T': 9.67,
        'U': 2.92, 'V': 0.82, 'W': 2.6, 'X': 0.11, 'Y': 2.04,
        'Z': 0.06
    }
    # sort dictionary by value in reverse order
    freq_dist_table = dict(sorted(freq_dist_table.items(), key=lambda x: x[1], reverse=True))
    print("Sorted frequency distribution table: ", freq_dist_table)

    # `Find percentiles of each presented character
    char_percentiles = [0.0]*26
    length = len(text)
    # number_of_char = 0

    # count characters
    for i in range(length):
        if str.isalpha(text[i]):
            char_percentiles[ord(text[i])-65] += 1
            # number_of_char += 1

    # print(length)
    # print(number_of_char)
    # determine percentiles
    text_percentiles_dict = dict()
    for i in range(26):
        # text_percentiles_dict[chr(i+65)] = round((char_percentiles[i]*100/number_of_char), 2)
        text_percentiles_dict[chr(i+65)] = round((char_percentiles[i]*100/length), 2)

    # sorting the percentile dictionary in reverse order for better comparison
    text_percentiles_dict = dict(sorted(text_percentiles_dict.items(), key=lambda x: x[1], reverse=True))
    print('Sorted frequency distribution for text' + str(number)+":", text_percentiles_dict)
    print('\n')
    return get_plaintext(text, number)


if __name__ == "__main__":
    # text = input("Enter the text: ")
    text1 = """
    IT CNJ FGM ETKMNOF CITMITK MIT JWF JIGFT GK YGK MINM SNMMTK CITMITK
    OM CNJ ZNB GK FOUIM IT CNJ NJINSTZ MG NJQ NDD MIT HDNFTM JTTSTZ MG DOXT
    RTFTNMI STMND MIT STND GY CIOEI IT INZ PWJM HNKMNQTF INZ RTTF DNRTDTZ
    DWFEITGF RWM MITKT CTKT SNFB HDNFTMJ CIOEI DOXTZ N JMNFZNKZ MOSTJENDT MINM
    MGGQ FG NEEGWFM GY MIT HTKINHJ OFEGFXTFOTFM NDMTKFNMOGF GY ZNB NFZ
    FOUIM. MIT KNMT GY HDNFTMNKB MWKFOFUJ ZOYYTKTZ, NFZ IT ZOZ FGM QFGC MINM
    GY MKNFMGK"""

    text2 = """
    VDUMU NEC E NEFF EDUEY SV ZUOEH DSOD SH VDU ESM EHY URVUHYUY
    BKNEMY LBV LI CSODV SV NEC MSYYFUY NSVD DLFUC VDEV NUMU VDU GLBVDC LI
    VBHHUFC OEEF'C VERS GLAUY VLNEMY LHU, VDUH KFBHOUY SHVL SV ILM E GLGUHV OEEF
    NLHYUMUY SYFP DLN DSC YMSAUM TLBFY KSTX LBV LHU EGLHO CL GEHP VDUMU NEC HLN
    LHFP ZFETXHUCC NSVD HLVDSHO ZBV VDU KECV-IFECDSHO LI E TLFLMUY CSOHEF FSODV VL
    MUFSUAU VDU OFLLG VDU ESM NEC IBFF LI E MBCDSHO CLBHY OEEF FUEHUY ILMNEMY
    EOESHCV YUTUFUMEVSLH VDUH EHY VDU VERS KLKKUY LBV LI VDU VBHHUF EHY
    YUCTUHYUY VL OMLBHY-FUAUF LHTU GLMU VDU FBRLM DLVUF CESY VDU YMSAUM
    BHHUTUCCEMSFP DU DUFKUY OEEF NSVD DSC ZEOOEOU ETTUKVUY E VUHVD-TMUYSV VSK
    NSVD E ZBCSHUCCFSXU ESM KSTXUY BK E NESVSHO KECCUHOUM EHY NEC MSCSHO EOESH
    SH EFF VDSC IMLG VDU GLGUHV LI YUZEMXEVSLH VDUMU DEY ZUUH HL OFSGKCU LI CXP
    VMEHVLM EV VDU ZUOSHHSHO LI VDU VDSMVUUHVD GSFFUHHSBG VDSC VUHYUHTP
    MUETDUY SVC TFSGER EC VDU TUHVUM LI VDU SGKUMSEF OLAUMHGUHV ILM BHZMLXUH
    DBHYMUYC LI OUHUMEVSLHC EHY FLTEVUY EC SV NEC VLNEMY VDU TUHVMEF MUOSLHC
    LI VDU OEFERP EGLHO VDU GLCV YUHCUFP KLKBFEVUY EHY SHYBCVMSEFFP EYAEHTUY
    NLMFYC LI VDU CPCVUG, SV TLBFY CTEMTUFP DUFK ZUSHO VDU YUHCUCV EHY MSTDUCV
    TFLV LI DBGEHSVP VDU METU DEY UAUM CUUH SVC BMZEHSQEVSLH, KMLOMUCCSHO
    CVUEYSFP DEY ISHEFFP MUETDUY VDU BFVSGEVU. EFF VDU FEHY CBMIETU LI VMEHVLM
    CJBEMU GSFUC SH URVUHV NEC E CSHOFU TSVP VDU KLKBFEVSLH EV SVC DUSODV NEC
    NUFF SH URTUCC LI ILMVP ZSFFSLHC VDSC UHLMGLBC KLKBFEVSLH NEC YUALVUY EFGLCV
    UHVSMUFP VL VDU EYGSHSCVMEVSAU HUTUCCSVSUC LI UGKSMU EHY ILBHY
    VDUGCUFAUC EFF VLL IUN ILM VDU TLGKFSTEVSLHC LI VDU VECX (SV SC VL ZU
    MUGUGZUMUY VDEV VDU SGKLCCSZSFSVP LI KMLKUM EYGSHSCVMEVSLH LI VDU
    OEFETVST UGKSMU BHYUM VDU BHSHCKSMUY FUEYUMCDSK LI VDU FEVUM UGKUMLMC
    NEC E TLHCSYUMEZFU IETVLM SH VDU IEFF) YESFP IFUUVC LI CDSKC SH VDU VUHC LI
    VDLBCEHYC ZMLBODV VDU KMLYBTU LI VNUHVP EOMSTBFVBMEF NLMFYC VL VDU
    YSHHUM VEZFUC LI VMEHVLM SVC YUKUHYUHTU BKLH VDU LBVUM NLMFYC ILM ILLY EHY
    SHYUUY ILM EFF HUTUCCSVSUC LI FSIU GEYU VMEHVLM SHTMUECSHOFP ABFHUMEZFU VL
    TLHJBUCV ZP CSUOU SH VDU FECV GSFFUHHSBG LI VDU UGKSMU VDU GLHLVLHLBCFP
    HBGUMLBC MUALFVC GEYU UGKUMLM EIVUM UGKUMLM TLHCTSLBC LI VDSC EHY
    SGKUMSEF KLFSTP ZUTEGU FSVVFU GLMU VDEH VDU KMLVUTVSLH LI VMEHVLM'C
    YUFSTEVU WBOBFEM AUSH"""


    print("Plain text for text 1:", decipher(text1, 1))
    print('\n\n')
    print("Plain text for text 2:", decipher(text2, 2))

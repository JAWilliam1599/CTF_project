package com.example.babydroid;

/* loaded from: classes3.dex */
public class Helper {
    public static String ran(String s) {
        String out = "";
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'm') {
                c = (char) (c + '\r');
            } else if (c >= 'A' && c <= 'M') {
                c = (char) (c + '\r');
            } else if (c >= 'n' && c <= 'z') {
                c = (char) (c - '\r');
            } else if (c >= 'N' && c <= 'Z') {
                c = (char) (c - '\r');
            }
            out = out + c;
        }
        return out;
    }

    public static String retriever() {
        StringBuilder sb;
        String str;
        String r = "";
        boolean upper = true;
        for (int i = 0; i < 26; i++) {
            if (upper) {
                sb = new StringBuilder();
                sb.append(r);
                str = "[A-Z_]";
            } else {
                sb = new StringBuilder();
                sb.append(r);
                str = "[a-z_]";
            }
            sb.append(str);
            r = sb.toString();
            upper = !upper;
        }
        return r;
    }
}

package com.example.babydroid;

import android.content.Context;

/* loaded from: classes3.dex */
public class FlagValidator {
    public static boolean checkFlag(Context ctx, String flag) {
        String result = Helper.retriever();
        if (flag.startsWith("HCMUS-CTF{") && flag.charAt(19) == '_' && flag.length() == 37 && flag.toLowerCase().substring(10).startsWith("this_is_") && flag.charAt(((int) (MagicNum.obtainY() * Math.pow(MagicNum.obtainX(), MagicNum.obtainY()))) + 2) == flag.charAt(((int) Math.pow(Math.pow(2.0d, 2.0d), 2.0d)) + 3) && new StringBuilder(flag).reverse().toString().toLowerCase().substring(1).startsWith(ctx.getString(R.string.last_part)) && new StringBuilder(flag).reverse().toString().charAt(0) == '}' && Helper.ran(flag.toUpperCase().substring((MagicNum.obtainY() * MagicNum.obtainX() * MagicNum.obtainY()) + 2, (int) (Math.pow(MagicNum.obtainZ(), MagicNum.obtainX()) + 1.0d))).equals("ERNYYL") && flag.toLowerCase().charAt(18) == 'a' && flag.charAt(18) == flag.charAt(28) && flag.toUpperCase().charAt(27) == flag.toUpperCase().charAt(28) + 1) {
            return flag.substring(10, flag.length() - 1).matches(result);
        }
        return false;
    }
}

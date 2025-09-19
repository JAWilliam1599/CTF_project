package com.example.babydroid;

import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.internal.view.SupportMenu;

/* loaded from: classes3.dex */
public class MainActivity extends AppCompatActivity {
    TextView mResultWidget = null;

    @Override // androidx.fragment.app.FragmentActivity, androidx.activity.ComponentActivity, androidx.core.app.ComponentActivity, android.app.Activity
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final EditText flagWidget = (EditText) findViewById(R.id.flag);
        Button checkFlag = (Button) findViewById(R.id.checkflag);
        final TextView resultWidget = (TextView) findViewById(R.id.result);
        this.mResultWidget = resultWidget;
        flagWidget.addTextChangedListener(new TextWatcher() { // from class: com.example.babydroid.MainActivity.1
            @Override // android.text.TextWatcher
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }

            @Override // android.text.TextWatcher
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                MainActivity.this.mResultWidget.setText("");
            }

            @Override // android.text.TextWatcher
            public void afterTextChanged(Editable s) {
            }
        });
        checkFlag.setOnClickListener(new View.OnClickListener() { // from class: com.example.babydroid.MainActivity.2
            @Override // android.view.View.OnClickListener
            public void onClick(View v) {
                String msg;
                int color;
                String flag = flagWidget.getText().toString();
                boolean result = FlagValidator.checkFlag(MainActivity.this, flag);
                if (result) {
                    msg = "Valid flag!";
                    color = -16737536;
                } else {
                    msg = "Invalid flag";
                    color = SupportMenu.CATEGORY_MASK;
                }
                resultWidget.setText(msg);
                resultWidget.setTextColor(color);
            }
        });
    }
}

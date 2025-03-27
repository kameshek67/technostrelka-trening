package com.example.message.activity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.AppCompatButton;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.example.message.R;
import com.example.message.model.User;
import com.example.message.retrofit.Api;
import com.example.message.retrofit.RetrofitService;
import com.google.android.material.textfield.TextInputEditText;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class SignInActivity extends AppCompatActivity {
    TextInputEditText signin_password_input, signin_email_input;
    AppCompatButton signin_auth;
    TextView signin_bottom_click;
    Intent RegisterActivity, HomeActivity;

    @SuppressLint({"WrongViewCast", "MissingInflatedId"})
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_sign_in);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });


        RegisterActivity = new Intent(this, RegisterActivity.class);
        HomeActivity = new Intent(this, HomeActivity.class);


        signin_bottom_click = findViewById(R.id.signin_bottom_click);
        signin_auth = findViewById(R.id.signin_auth);
        signin_email_input = findViewById(R.id.signin_email_input);
        signin_password_input = findViewById(R.id.signin_password_input);


        signin_auth.setOnClickListener(view -> {
            Api api = RetrofitService.initRetrofit().create(Api.class);

            String email = String.valueOf(signin_email_input.getText());
            String password = String.valueOf(signin_password_input.getText());

            User user = new User(email, password);

            Call<ResponseBody> call = api.signin("password",
                    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imprc2Zqa3Jkd3Vhbm9tbWZnY2hyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDEzNzQxOTAsImV4cCI6MjA1Njk1MDE5MH0.b49BcB-adIVODY3H_kW-7S5vckJm7Z5eSvnotH1hrFI",
                    "application/json",
                    user);
            call.enqueue(new Callback<ResponseBody>() {
                @Override
                public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                    if (response.isSuccessful()) {
                        startActivity(new Intent(SignInActivity.this, HomeActivity.class));
                    }
                }

                @Override
                public void onFailure(Call<ResponseBody> call, Throwable throwable) {

                }
            });
        });


        signin_bottom_click.setOnClickListener(view -> {
            startActivity(RegisterActivity);
        });
    }
}







package com.example.message.retrofit;

import com.example.message.model.User;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.Header;
import retrofit2.http.POST;
import retrofit2.http.Query;

public interface Api {

    @POST("/authorization")
    Call<ResponseBody> signin(
            @Query("login") String login, @Query("password") String password
    );

}

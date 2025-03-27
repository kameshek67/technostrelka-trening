package com.example.message.retrofit;

import com.example.message.model.User;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.Header;
import retrofit2.http.POST;
import retrofit2.http.Query;

public interface Api {

    @POST("auth/v1/token")
    Call<ResponseBody> signin(
            @Query("grant_type") String grant_type,
            @Header("apikey") String apikey,
            @Header("Content-Type") String contentType,
            @Body User user
    );

}

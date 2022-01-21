package com.ds13.anitracker;

import static com.ds13.anitracker.NetworkService.getBaseUrl;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class Anime {
    @SerializedName("pk")
    @Expose
    private int pk;

    @SerializedName("title")
    @Expose
    private String title;

    @SerializedName("poster")
    @Expose
    private String poster;

    @SerializedName("description")
    @Expose
    private String description;

    @SerializedName("status")
    @Expose
    private String status;

    @SerializedName("interest")
    @Expose
    private String interest;

    public int getPk() {
        return pk;
    }

    public String getTitle() {
        return title;
    }

    public String getPoster() {
//        return getBaseUrl() + poster.substring("http://localhost:8000".length());
        return poster;
    }

    public String getDescription() {
        return description;
    }

    public String getStatus() {
        return status;
    }

    public String getInterest() {
        return interest;
    }
}

package com.etech.myoa.view;

import com.etech.myoa.R;

import android.app.DialogFragment;  
import android.os.Bundle;  
import android.view.LayoutInflater;  
import android.view.View;  
import android.view.ViewGroup;  
  
public class MyDialog extends DialogFragment{  
  
    @Override  
    public View onCreateView(LayoutInflater inflater, ViewGroup container,  
            Bundle savedInstanceState){  
        View view = inflater.inflate(R.layout.dialog_test, container, false);  
        return view;  
    }  
  
}  
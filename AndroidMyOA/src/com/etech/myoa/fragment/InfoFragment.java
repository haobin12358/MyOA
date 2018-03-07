package com.etech.myoa.fragment;

import com.etech.myoa.activity.MainActivity;

import android.app.Fragment;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

public class InfoFragment extends Fragment{
	
	private String Uid;

	public View onCreateView(LayoutInflater inflater, ViewGroup container,
			Bundle savedInstanceState) {
		getBd();
		View view = null;
		return view;
	}
	
	private void getBd(){
		Uid = ((MainActivity)getActivity()).getUid();
		//Utype = ((MainActivity)getActivity()).getUtype();
		//index = ((MainActivity)getActivity()).getIndex();
	}

}

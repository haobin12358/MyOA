package com.etech.myoa.fragment;

import com.etech.myoa.activity.MainActivity;

import android.app.Fragment;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

public class ApprovalsFragment extends Fragment{
	
	private String Uid;
	private int isManager;

	public View onCreateView(LayoutInflater inflater, ViewGroup container,
			Bundle savedInstanceState) {
		getBd();
		View view = null;
		return view;
	}
	
	private void getBd(){
		Uid = ((MainActivity)getActivity()).getUid();
		isManager = ((MainActivity)getActivity()).getisManager();
		//index = ((MainActivity)getActivity()).getIndex();
	}
}

package com.etech.myoa.activity;

import com.etech.myoa.R;
import com.etech.myoa.fragment.ApprovalsFragment;
import com.etech.myoa.fragment.DocumentFragment;
import com.etech.myoa.fragment.InfoFragment;
import com.etech.myoa.fragment.MeFragment;
import android.app.Activity;
import android.app.FragmentTransaction;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.TextView;

public class MainActivity extends Activity {

	//�����������
	private TextView tv1, tv2, tv3, tv4;
	//����Ĭ�ϲ���
	public int index = 0;
	public String Uid;
	public int Utype;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
	}
	
	public String getUid(){
		return Uid;
	}
	public int getUtype(){
		return Utype;
	}
	public int getIndex(){
		return index;
	}
	
	//ע���������
	private void init(){
		tv1 = (TextView)findViewById(R.id.bar_text1);
		tv2 = (TextView)findViewById(R.id.bar_text2);
		tv3 = (TextView)findViewById(R.id.bar_text3);
		tv4 = (TextView)findViewById(R.id.bar_text4);
	}
	
	//������Ӧ�¼�
	private void setListener(){
		tv1.setOnClickListener(tabClickListener);
		tv2.setOnClickListener(tabClickListener);
		findViewById(R.id.bar_text3).setOnClickListener(tabClickListener);
		tv4.setOnClickListener(tabClickListener);
	}
	
	//��ȡ����һ�����洫����ֵ
	private void getBd(){
		Intent intent = getIntent();
		try{
			Bundle bd = intent.getExtras();
			int n = bd.getInt("index");
			if (n == 0 || n == 1 || n == 2) {
				index = n;
			}
			Uid = bd.getString("Uid");
			Utype = bd.getInt("Utype");
		}catch (Exception e) {
			e.printStackTrace();
			Log.e("changeError", "false");
			index = 2;
		}
	}
	
	//�ײ���������Ӧ�¼�
	private OnClickListener tabClickListener = new OnClickListener(){

		@Override
		public void onClick(View v) {
		// TODO Auto-generated method stub
			switch(v.getId()){
			case R.id.bar_text1:
				setTextColorChecked(tv1, 0);
				setTextColorUnChecked(tv2, 1);
				setTextColorUnChecked(tv3, 2);
				setTextColorUnChecked(tv4, 3);
				SwitchFragment(0);
				break;
			case R.id.bar_text2:
				setTextColorUnChecked(tv1, 0);
				setTextColorChecked(tv2, 1);
				setTextColorUnChecked(tv3, 2);
				setTextColorUnChecked(tv4, 3);
				SwitchFragment(1);
				break;
			case R.id.bar_text3:
				setTextColorUnChecked(tv1, 0);
				setTextColorUnChecked(tv2, 1);
				setTextColorChecked(tv3, 2);
				setTextColorUnChecked(tv4, 3);
				SwitchFragment(2);
				break;
			case R.id.bar_text4:
				setTextColorUnChecked(tv1, 0);
				setTextColorUnChecked(tv2, 1);
				setTextColorUnChecked(tv3, 2);
				setTextColorChecked(tv4, 3);
				SwitchFragment(3);
				break;
			}
		}
			
	};
		
	//�ײ���������ɫ�仯���ܣ������
	private void setTextColorChecked(TextView tv, int index){
		tv.setTextColor(getResources().getColor(R.color.mainactivity_click_red));
		if(index == 0){
			tv.setCompoundDrawablesWithIntrinsicBounds(null,getResources()
					.getDrawable(R.drawable.ic_main_tab_1_p), null, null);
		}else if(index == 1){
			tv.setCompoundDrawablesWithIntrinsicBounds(null,getResources()
					.getDrawable(R.drawable.ic_main_tab_2_p), null, null);
		}else if(index == 2){
			tv.setCompoundDrawablesWithIntrinsicBounds(null,getResources()
					.getDrawable(R.drawable.ic_main_tab_3_p), null, null);
		}else if(index == 3){
			tv.setCompoundDrawablesWithIntrinsicBounds(null,getResources()
					.getDrawable(R.drawable.ic_main_tab_4_p), null, null);
		}
	}
	
	//�ײ���������ɫ�仯���ܣ����ǰ��
	private void setTextColorUnChecked(TextView tv, int index){
		tv.setTextColor(getResources().getColor(R.color.mainactivity_unclick_gray));
		if(index == 0){
			tv.setCompoundDrawablesWithIntrinsicBounds(null,getResources()
					.getDrawable(R.drawable.ic_main_tab_1), null, null);
		}else if(index == 1){
			tv.setCompoundDrawablesWithIntrinsicBounds(null,getResources()
					.getDrawable(R.drawable.ic_main_tab_2), null, null);
		}else if(index == 2){
			tv.setCompoundDrawablesWithIntrinsicBounds(null,getResources()
					.getDrawable(R.drawable.ic_main_tab_3), null, null);
		}else if(index == 3){
			tv.setCompoundDrawablesWithIntrinsicBounds(null,getResources()
					.getDrawable(R.drawable.ic_main_tab_4), null, null);
		}
	}
	
	//����fragment������ʵ�־�����湦��
	private ApprovalsFragment f1;
	private DocumentFragment f2;
	private InfoFragment f3;
	private MeFragment f4;
	
	//�ײ��������л�����
	private void SwitchFragment(int id){
		FragmentTransaction transaction = this.getFragmentManager()
				.beginTransaction();
		switch(id){
		case 0:
			hideFragment(transaction);
			if(f1 == null){
				f1 = new ApprovalsFragment();
				transaction.add(R.id.fl_fragment_layout, f1);
			}
			transaction.show(f1);
			break;
		case 1:
			hideFragment(transaction);
			if(f2 == null){
				f2 = new DocumentFragment();
				transaction.add(R.id.fl_fragment_layout, f2);
			}
			transaction.show(f2);
			break;
		case 2:
			hideFragment(transaction);
			if(f3 == null){
				f3 = new InfoFragment();
				transaction.add(R.id.fl_fragment_layout, f3);
			}
			transaction.show(f3);
			break;
		case 3:
			hideFragment(transaction);
			if(f4 == null){
				f4 = new MeFragment();
				transaction.add(R.id.fl_fragment_layout, f4);
			}
			transaction.show(f4);
			break;
		}
		transaction.commitAllowingStateLoss();
	}

	//����fragment����
	private void hideFragment(FragmentTransaction transaction){
		
		if(f1 != null){
			transaction.hide(f1);
		}
		if(f2 != null){
			transaction.hide(f2);
		}
		if(f3 != null){
			transaction.hide(f3);
		}
		if(f4 != null){
			transaction.hide(f4);
		}
	}
}

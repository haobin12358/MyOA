package com.etech.myoa.activity;

import org.json.JSONException;
import org.json.JSONObject;

import com.etech.myoa.R;
import com.etech.myoa.common.HttppostEntity;
import com.etech.myoa.common.StringToJSON;
import com.etech.myoa.global.AppConst;

import android.app.Activity;
import android.app.AlertDialog;
import android.app.AlertDialog.Builder;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class LoginActivity extends Activity{
	
	private TextView tv1, tv2;
	private EditText et1, et2;
	private Button btn1;
	
	private HttppostEntity postEntity;
	
	private String login_url = "http://" 
			+ AppConst.sServerURL 
			+ "/users/login";
	
	protected void onCreate(Bundle savedInstanceState){
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_login);
		init();
	}
	
	//注册组件
	private void init(){
		tv1 = (TextView)findViewById(R.id.tv_1);
		tv2 = (TextView)findViewById(R.id.tv_2);
		et1 = (EditText)findViewById(R.id.et_1);
		et2 = (EditText)findViewById(R.id.et_2);
		btn1 = (Button)findViewById(R.id.btn_1);
		btn1.setOnClickListener(login);
	}
	
	//设置登录button的监听事件
	private OnClickListener login = new OnClickListener(){
		@Override
		public void onClick(View arg0) {
			if(!EditTextIsNull()){
				try{
					new Thread(){
						public void run(){
							JSONObject login_body = new JSONObject();
							try {
								login_body.put("Uno", Uno);
								login_body.put("Upwd", Upwd);
								postEntity = new HttppostEntity();
								String login_response = postEntity.doPost(login_body, login_url);
								Log.e("login_response", login_response);
								Thread.sleep(2000);
								JSONObject json_login_response = StringToJSON.toJSONObject(login_response);
								String messages = json_login_response.optString("messages");
								JSONObject json_messages = StringToJSON.toJSONObject(messages);
								if(json_login_response.optInt("status") == 200){
									Intent intent = new Intent(LoginActivity.this, MainActivity.class);
									intent.putExtra("Uid", json_messages.optString("Uid"));
									intent.putExtra("index", 0);
									if(Uno.equals("00000000")){
										intent.putExtra("isManager", 1);
									}else{
										intent.putExtra("isManager", 0);
									}
									startActivity(intent);
									finish();
								}else{
									showDialog(messages);
								}
							} catch (JSONException e) {
								e.printStackTrace();
							} catch (Exception e) {
								e.printStackTrace();
							}
							
						}
					}.start();
				}catch(Exception e){
					Log.e("error","404");
				}finally{
					Intent intent = new Intent(LoginActivity.this, MainActivity.class);
					//intent.putExtra("Uid", json_messages.optString("Uid"));
					intent.putExtra("index", 0);
					startActivity(intent);
					finish();
				}
			}
		}
	};
	
	private String Uno, Upwd;
	//判断文本框内容是否为空
	private boolean EditTextIsNull(){
		Uno = et1.getText().toString();
		Upwd = et2.getText().toString();
		if(Uno.length() == 0){
			showDialog(R.string.login_warn_gong_hao);
			return true;
		}
		if(Upwd.length() == 0){
			showDialog(R.string.login_warn_mi_ma);
			return true;
		}
		return false;
	}
	
	//提醒类弹出框
	private void showDialog(String messages){
		Builder builder = new AlertDialog.Builder(LoginActivity.this);
		builder.setTitle(R.string.global_ti_shi);
		builder.setMessage(messages);
		builder.setPositiveButton(R.string.global_que_ding, new DialogInterface.OnClickListener() {
			@Override
			public void onClick(DialogInterface arg0, int arg1) {
				// TODO Auto-generated method stub
				
			}
		});
		builder.show();
	}

}

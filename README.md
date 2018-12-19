# TOC Project

Template Code for TOC Project

A Facebook messenger bot based on a finite state machine

More details in the [Slides](https://hackmd.io/p/SkpBR-Yam#/) and [FAQ](https://hackmd.io/s/B1Xw7E8kN)

## Setup

### Prerequisite
* Python 3
* Facebook Page and App
* HTTPS Server

#### Install Dependency
```sh
pip3 install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

#### Secret Data

`VERIFY_TOKEN` and `ACCESS_TOKEN` **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
./ngrok http 5000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: anything
		* user state will directly go to state0
		* Reply: "歡迎來到雙主修選課系統，請選擇您的科系（機械/資工）"
* useless 1 and 2
		* no any reply no function,in order to reach ta's requirement
* state0
	* Input: 機械
		* state0 will go to state1
		* change var major=1(represent me)
		* Reply: "請選擇查詢必修或是查詢擋修（必修/擋修）"
* state1
	* Input: 必修
		* state1 will go to state2
		* Reply: "請選擇年級（ex:一年級）"
* state1
	* Input: 擋修
		* state1 will go to state6
		* Reply: pic of bolocking tree
* state2&8
	* Input: 一年級
            * state2 will go to state3
            if major=1 
		* Reply: "一上：微積分一、普化、靜力學、普物一/一下：微積分二、工程圖學、動力學、普物二"
            if major=2 
		* Reply: "一上：微積分一、程式設計一、計算機概論、普物一/一下：微積分二、程式設計二、普物二、數位電路導論"
* state2&8
	* Input: 二年級
		* state2 will go to state4
            if major=1 
		* Reply: "二上：工程數學一、熱力學一、材料力學一、機動學一/二下：工程數學二、熱力學二、機械製造、機動學二、電工學"
            if major=2 
		* Reply: "二上：數位系統、資料結構、工程數學、數位系統實驗/二下：離散數學、計算機組織、機率與統計"
* state2&8
	* Input: 三年級
		* state2 will go to state5
            if major=1 
		* Reply: "三上：自動控制、流體力學、機械設計、電子學/三下：機工實驗、熱傳學、專題實作"
            if major=2 
		* Reply: "三上：演算法、作業系統、微算機原理與應用(含實驗)、計算理論/三下：程式語言、編譯系統、資訊專題（一）"
* state0
	* Input: 資工
		* state0 will go to state7
		* change var major=2(represent csie)
		* Reply: "請選擇查詢必修或是查詢選修（必修/選修"
* state7
	* Input: 必修
		* state7 will go to state8
		* Reply: "請選擇年級（ex:一年級）"
* state3&4&5&6
	* Input: nothing(go_back)
		* state3456 will go to final
		* Reply: nothing
* state7
	* Input: nothing(again)
		* final will go to user
		* Reply: nothing


## Reference
[TOC-Project-2017](https://github.com/Lee-W/TOC-Project-2017) ❤️ [@Lee-W](https://github.com/Lee-W)

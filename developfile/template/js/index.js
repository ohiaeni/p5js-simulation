///全画面表示
function fullScreen() {
    createCanvas(windowWidth, 9 * windowHeight / 10)
}

// 外部ファイルの読み込み
function preload() {

}

// DOM要素の生成
function elCreate() {

}

// DOM要素の設定
function elInit() {

}

// 初期値やシミュレーションの設定
function initValue() {

}

// setup関数
function setup() {
    fullScreen()
    elCreate()
    elInit()
    initValue()
}

// draw関数
function draw() {
    background(100)
}

// windowがリサイズされたときの処理
function windowResized() {
    fullScreen()
    elInit()
    initValue()
}

// class Sample{

// }
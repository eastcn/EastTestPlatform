# unittest & pytest demo
## PT（pytest）
## UT（unittest）
### 基本概念
#### test case
即一个基本的测试case，包括前置环境准备、测试执行、测试结束释放。  
在unittest中提供了基类：TestCase
#### test suit
即测试用例集，可用于归档多个基本case或者用例集
#### test runner
测试用例执行
#### test fixture
测试脚手架，可以实现一些测试用例中的前期搭建或者使用结束的还原操作，主要用于实现一些在测试执行步骤以外的动作。

### [简单demo](./UT/testCases/testSimpleCase.py)
1. 在unittest中，新建一个测试case都需要继承基类：TestCase  
2. test case 中以test作为命名开头的方法都会被识别为一个测试执行方法
3. 基类TestCase中的setUp和tearDown方法重写后，执行时会直接调用
4. unittest.main()，是unittest的调用入口，该方法会执行所有的case
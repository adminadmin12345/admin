import allure
import pytest

class  Test_01:
    @allure.step(title="测试步骤001")
    @pytest.mark.parametrize("a", [1,2,3,4,5])
    def test_001(self,a):
        allure.attach("描述", "我是测试步骤的第一步")
        assert  a !=1

    # @pytest.allure.serverity(pytest.allure.serverity_level.CRITICAL)
    # @allure.step(title="测试步骤002")
    # @pytest.mark.parametrize("a",[1,2,3])
    # def test_abc(self,a):
    #     allure.attach("描述","我是测试步骤的第二步")
    #     assert  a !=2


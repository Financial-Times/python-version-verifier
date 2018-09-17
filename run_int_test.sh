#!/usr/bin/env bash

######## Functions #########
int_test() {
  python_ver=${1}
  expected_lambda_message=${2}

  result="$(${python_ver} tests/lambda_sample.py)"

  # We want the pass message as lambda has correct python version
  if ( echo $result | grep -q "${expected_lambda_message}" ); then
    echo "Integration test passed \nResponse from lambda: \n${result}"
  else
    echo "Integration test failed \nResponse from lambda: \n${result}"
  fi
}

ERROR="Detected Python 2.7. Python 3.6 or above is required, \
please update python to v3.6 or higher"
PASS="version check passed"


echo -e "\n\n####### testing lambda with python v3.6 #######"
response=$(int_test "python3" "${PASS}")
echo -e ${response}

echo -e "\n\n####### testing lambda with python v2.7 #######"
response=$(int_test "python" "${ERROR}")
echo -e ${response}

# ### Debug ####
# # make sure string comparison is working
# # This should return as a failure
# echo -e "\n\n####### testing string comparison logic - this will fail #######"
# response=$(int_test "python" "${PASS}")
# echo -e ${response}

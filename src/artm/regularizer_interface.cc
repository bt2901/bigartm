// Copyright 2014, Additive Regularization of Topic Models.

#include "artm/regularizer_interface.h"

#include "artm/core/dictionary.h"
#include "artm/core/instance.h"
#include "artm/core/phi_matrix.h"

namespace artm {

std::shared_ptr< ::artm::core::Dictionary> RegularizerInterface::dictionary(const std::string& dictionary_name) {
  return ::artm::core::ThreadSafeDictionaryCollection::singleton().get(dictionary_name);
}

std::shared_ptr<const ::artm::core::PhiMatrix> RegularizerInterface::GetPhiMatrix(const std::string& model_name) {
    return instance_->GetPhiMatrixSafe(model_name);
}

std::shared_ptr<const ::artm::core::PhiMatrix> RegularizerInterface::GetPhiMatrix() {
    return GetPhiMatrix(instance_->config()->nwt_name());
}

}  // namespace artm

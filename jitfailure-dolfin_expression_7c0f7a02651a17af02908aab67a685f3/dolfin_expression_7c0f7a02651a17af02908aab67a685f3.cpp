
// Based on https://gcc.gnu.org/wiki/Visibility
#if defined _WIN32 || defined __CYGWIN__
    #ifdef __GNUC__
        #define DLL_EXPORT __attribute__ ((dllexport))
    #else
        #define DLL_EXPORT __declspec(dllexport)
    #endif
#else
    #define DLL_EXPORT __attribute__ ((visibility ("default")))
#endif

#include <dolfin/function/Expression.h>
#include <dolfin/math/basic.h>
#include <Eigen/Dense>


// cmath functions
using std::cos;
using std::sin;
using std::tan;
using std::acos;
using std::asin;
using std::atan;
using std::atan2;
using std::cosh;
using std::sinh;
using std::tanh;
using std::exp;
using std::frexp;
using std::ldexp;
using std::log;
using std::log10;
using std::modf;
using std::pow;
using std::sqrt;
using std::ceil;
using std::fabs;
using std::floor;
using std::fmod;
using std::max;
using std::min;

const double pi = DOLFIN_PI;


namespace dolfin
{
  class dolfin_expression_7c0f7a02651a17af02908aab67a685f3 : public Expression
  {
     public:
       double t;


       dolfin_expression_7c0f7a02651a17af02908aab67a685f3()
       {
            
       }

       void eval(Eigen::Ref<Eigen::VectorXd> values, Eigen::Ref<const Eigen::VectorXd> x) const override
       {
          values[0] = // Not supported in C:
// ImmutableDenseNDimArray
[0.0, 3.5e+19, 7.0e+19, 1.05e+20, 1.4e+20, 1.75e+20, 2.1e+20, 2.45e+20, 2.8e+20, 3.15e+20, 3.5e+20, 3.85e+20, 4.2e+20, 4.55e+20, 4.9e+20, 5.25e+20, 5.6e+20, 5.95e+20, 6.3e+20, 6.65e+20, 7.0e+20, 7.35e+20, 7.7e+20, 8.05e+20, 8.4e+20, 8.75e+20, 9.1e+20, 9.45e+20, 9.8e+20, 1.015e+21, 1.05e+21, 1.085e+21, 1.12e+21, 1.155e+21, 1.19e+21, 1.225e+21, 1.26e+21, 1.295e+21, 1.33e+21, 1.365e+21, 1.4e+21, 1.435e+21, 1.47e+21, 1.505e+21, 1.54e+21, 1.575e+21, 1.61e+21, 1.645e+21, 1.68e+21, 1.715e+21, 1.75e+21, 1.785e+21, 1.82e+21, 1.855e+21, 1.89e+21, 1.925e+21, 1.96e+21, 1.995e+21, 2.03e+21, 2.065e+21, 2.1e+21, 2.135e+21, 2.17e+21, 2.205e+21, 2.24e+21, 2.275e+21, 2.31e+21, 2.345e+21, 2.38e+21, 2.415e+21, 2.45e+21, 2.485e+21, 2.52e+21, 2.555e+21, 2.59e+21, 2.625e+21, 2.66e+21, 2.695e+21, 2.73e+21, 2.765e+21, 2.8e+21, 2.835e+21, 2.87e+21, 2.905e+21, 2.94e+21, 2.975e+21, 3.01e+21, 3.045e+21, 3.08e+21, 3.115e+21, 3.15e+21, 3.185e+21, 3.22e+21, 3.255e+21, 3.29e+21, 3.325e+21, 3.36e+21, 3.395e+21, 3.43e+21, 3.465e+21];

       }

       void set_property(std::string name, double _value) override
       {
          if (name == "t") { t = _value; return; }
       throw std::runtime_error("No such property");
       }

       double get_property(std::string name) const override
       {
          if (name == "t") return t;
       throw std::runtime_error("No such property");
       return 0.0;
       }

       void set_generic_function(std::string name, std::shared_ptr<dolfin::GenericFunction> _value) override
       {

       throw std::runtime_error("No such property");
       }

       std::shared_ptr<dolfin::GenericFunction> get_generic_function(std::string name) const override
       {

       throw std::runtime_error("No such property");
       }

  };
}

extern "C" DLL_EXPORT dolfin::Expression * create_dolfin_expression_7c0f7a02651a17af02908aab67a685f3()
{
  return new dolfin::dolfin_expression_7c0f7a02651a17af02908aab67a685f3;
}


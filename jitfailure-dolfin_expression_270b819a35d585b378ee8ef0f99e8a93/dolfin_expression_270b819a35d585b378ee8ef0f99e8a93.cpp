
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
  class dolfin_expression_270b819a35d585b378ee8ef0f99e8a93 : public Expression
  {
     public:
       double t;


       dolfin_expression_270b819a35d585b378ee8ef0f99e8a93()
       {
            
       }

       void eval(Eigen::Ref<Eigen::VectorXd> values, Eigen::Ref<const Eigen::VectorXd> x) const override
       {
          values[0] = // Not supported in C:
// ImmutableDenseNDimArray
[0.0, 10000000000.0, 20000000000.0, 30000000000.0, 40000000000.0, 50000000000.0, 60000000000.0, 70000000000.0, 80000000000.0, 90000000000.0, 100000000000.0, 110000000000.0, 120000000000.0, 130000000000.0, 140000000000.0, 150000000000.0, 160000000000.0, 170000000000.0, 180000000000.0, 190000000000.0, 200000000000.0, 210000000000.0, 220000000000.0, 230000000000.0, 240000000000.0, 250000000000.0, 260000000000.0, 270000000000.0, 280000000000.0, 290000000000.0, 300000000000.0, 310000000000.0, 320000000000.0, 330000000000.0, 340000000000.0, 350000000000.0, 360000000000.0, 370000000000.0, 380000000000.0, 390000000000.0, 400000000000.0, 410000000000.0, 420000000000.0, 430000000000.0, 440000000000.0, 450000000000.0, 460000000000.0, 470000000000.0, 480000000000.0, 490000000000.0, 500000000000.0, 510000000000.0, 520000000000.0, 530000000000.0, 540000000000.0, 550000000000.0, 560000000000.0, 570000000000.0, 580000000000.0, 590000000000.0, 600000000000.0, 610000000000.0, 620000000000.0, 630000000000.0, 640000000000.0, 650000000000.0, 660000000000.0, 670000000000.0, 680000000000.0, 690000000000.0, 700000000000.0, 710000000000.0, 720000000000.0, 730000000000.0, 740000000000.0, 750000000000.0, 760000000000.0, 770000000000.0, 780000000000.0, 790000000000.0, 800000000000.0, 810000000000.0, 820000000000.0, 830000000000.0, 840000000000.0, 850000000000.0, 860000000000.0, 870000000000.0, 880000000000.0, 890000000000.0, 900000000000.0, 910000000000.0, 920000000000.0, 930000000000.0, 940000000000.0, 950000000000.0, 960000000000.0, 970000000000.0, 980000000000.0, 990000000000.0];

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

extern "C" DLL_EXPORT dolfin::Expression * create_dolfin_expression_270b819a35d585b378ee8ef0f99e8a93()
{
  return new dolfin::dolfin_expression_270b819a35d585b378ee8ef0f99e8a93;
}


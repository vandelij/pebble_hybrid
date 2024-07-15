
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
  class dolfin_expression_dcb1f6e8fdd6e8ca73526f2abc61f466 : public Expression
  {
     public:
       double t;


       dolfin_expression_dcb1f6e8fdd6e8ca73526f2abc61f466()
       {
            
       }

       void eval(Eigen::Ref<Eigen::VectorXd> values, Eigen::Ref<const Eigen::VectorXd> x) const override
       {
          values[0] = // Not supported in C:
// ImmutableDenseNDimArray
[1000000000.0, 1000000010.0, 1000000020.0, 1000000030.0, 1000000040.0, 1000000050.0, 1000000060.0, 1000000070.0, 1000000080.0, 1000000090.0, 1000000100.0, 1000000110.0, 1000000120.0, 1000000130.0, 1000000140.0, 1000000150.0, 1000000160.0, 1000000170.0, 1000000180.0, 1000000190.0, 1000000200.0, 1000000210.0, 1000000220.0, 1000000230.0, 1000000240.0, 1000000250.0, 1000000260.0, 1000000270.0, 1000000280.0, 1000000290.0, 1000000300.0, 1000000310.0, 1000000320.0, 1000000330.0, 1000000340.0, 1000000350.0, 1000000360.0, 1000000370.0, 1000000380.0, 1000000390.0, 1000000400.0, 1000000410.0, 1000000420.0, 1000000430.0, 1000000440.0, 1000000450.0, 1000000460.0, 1000000470.0, 1000000480.0, 1000000490.0, 1000000500.0, 1000000510.0, 1000000520.0, 1000000530.0, 1000000540.0, 1000000550.0, 1000000560.0, 1000000570.0, 1000000580.0, 1000000590.0, 1000000600.0, 1000000610.0, 1000000620.0, 1000000630.0, 1000000640.0, 1000000650.0, 1000000660.0, 1000000670.0, 1000000680.0, 1000000690.0, 1000000700.0, 1000000710.0, 1000000720.0, 1000000730.0, 1000000740.0, 1000000750.0, 1000000760.0, 1000000770.0, 1000000780.0, 1000000790.0, 1000000800.0, 1000000810.0, 1000000820.0, 1000000830.0, 1000000840.0, 1000000850.0, 1000000860.0, 1000000870.0, 1000000880.0, 1000000890.0, 1000000900.0, 1000000910.0, 1000000920.0, 1000000930.0, 1000000940.0, 1000000950.0, 1000000960.0, 1000000970.0, 1000000980.0, 1000000990.0];

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

extern "C" DLL_EXPORT dolfin::Expression * create_dolfin_expression_dcb1f6e8fdd6e8ca73526f2abc61f466()
{
  return new dolfin::dolfin_expression_dcb1f6e8fdd6e8ca73526f2abc61f466;
}

